"""
Interactive SSH command executor with pexpect-style API.

Pure paramiko — no pexpect dependency. Works on Windows and Linux.
Provides sendline(), expect(), collect_remaining() for driving multi-step
interactive prompts (password changes, confirmations, menus).

Includes SecretRedactor for log safety and MockChannel for unit testing.
"""

from __future__ import annotations

import logging
import os
import re
import time
from typing import Optional

logger = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# Exceptions
# ---------------------------------------------------------------------------

class PromptTimeout(Exception):
    """Expected prompt was not seen within the allowed timeout."""
    pass


# ---------------------------------------------------------------------------
# Secret Redaction
# ---------------------------------------------------------------------------

class SecretRedactor:
    """
    Tracks secret values and replaces them with '***' in any text.
    Register secrets via add(), then use redact() before logging.
    """

    def __init__(self):
        self._secrets: set[str] = set()

    def add(self, secret: str) -> None:
        if secret and not secret.startswith("<MISSING:"):
            self._secrets.add(secret)

    def redact(self, text: str) -> str:
        for s in self._secrets:
            text = text.replace(s, "***")
        return text


# ---------------------------------------------------------------------------
# InteractiveCommandRunner (pure paramiko)
# ---------------------------------------------------------------------------

class InteractiveCommandRunner:
    """
    Pexpect-like interface built on paramiko's invoke_shell().
    No pexpect dependency — uses only paramiko + stdlib.

    Usage::

        runner = InteractiveCommandRunner(ssh_client)
        runner.sendline("ipmcset -t user -d password -v testuser")
        runner.expect("current password:", timeout=10)
        runner.sendline("OldPass123!", redact=True)
        runner.expect("new password:", timeout=10)
        runner.sendline("NewPass456!", redact=True)
        runner.expect("confirm", timeout=10)
        runner.sendline("NewPass456!", redact=True)
        output = runner.collect_remaining(timeout=3)
        runner.close()
    """

    def __init__(
        self,
        ssh_client,
        width: int = 200,
        height: int = 50,
        banner_timeout: float = 2.0,
    ) -> None:
        self.channel = ssh_client.invoke_shell(width=width, height=height)
        self.channel.settimeout(0.1)
        self.buffer: str = ""
        self.full_output: str = ""
        self._expect_scan_pos: int = 0
        self.redactor = SecretRedactor()

        # Drain login banner so it doesn't pollute prompt matching
        self._drain(banner_timeout)
        self._expect_scan_pos = len(self.buffer)

    # -- Core API -----------------------------------------------------------

    def sendline(self, text: str, redact: bool = False) -> None:
        """Send a line (appends \\n). If redact=True, value is registered for log redaction."""
        if redact:
            resolved = self._resolve_env(text)
            self.redactor.add(resolved)
            logger.debug("SEND: ***")
        else:
            logger.debug("SEND: %s", text)
        actual = self._resolve_env(text)
        self.channel.send((actual + "\n").encode("utf-8"))

    def expect(self, pattern: str, timeout: float = 10.0) -> str:
        """
        Block until pattern appears in output (case-insensitive).

        Parameters:
            pattern:  Literal substring or regex.
            timeout:  Seconds to wait.

        Returns the full buffer at match point.
        Raises PromptTimeout if not found.
        """
        deadline = time.monotonic() + timeout
        scan_start = self._expect_scan_pos

        while time.monotonic() < deadline:
            chunk = self._read_chunk()
            if chunk:
                self.buffer += chunk
                self.full_output += chunk

            new_region = self.buffer[scan_start:]

            # Case-insensitive substring (fast path)
            lower_region = new_region.lower()
            lower_pattern = pattern.lower()
            if lower_pattern in lower_region:
                match_idx = lower_region.index(lower_pattern)
                self._expect_scan_pos = scan_start + match_idx + len(pattern)
                logger.debug("MATCH (substring): %r", pattern)
                return self.buffer

            # Regex fallback (case-insensitive)
            try:
                m = re.search(pattern, new_region, re.IGNORECASE)
                if m:
                    self._expect_scan_pos = scan_start + m.end()
                    logger.debug("MATCH (regex): %r", pattern)
                    return self.buffer
            except re.error:
                pass

            time.sleep(0.05)

        safe_tail = self.redactor.redact(self.buffer[-300:])
        raise PromptTimeout(
            f"Timeout after {timeout:.1f}s waiting for {pattern!r}.  "
            f"Buffer tail: …{safe_tail}"
        )

    def collect_remaining(self, timeout: float = 3.0) -> str:
        """Drain output for timeout seconds, return full_output."""
        self._drain(timeout)
        return self.full_output

    def close(self) -> None:
        try:
            self.channel.close()
        except Exception:
            pass

    # -- Convenience: run a full interactive plan ---------------------------

    def run_steps(
        self,
        initial_command: str,
        steps: list[dict],
        final_timeout: float = 3.0,
    ) -> tuple[bool, str]:
        """
        Execute initial_command, then walk through steps (expect/send pairs).

        Each step dict requires:
            expect_prompt:  str — substring or regex
            send_input:     str — text to send (may use $ENV{VAR})
            timeout_sec:    int — per-step timeout (REQUIRED, no default)
            is_secret:      bool — optional, redact from logs
        """
        try:
            self.sendline(initial_command)
            for step in steps:
                self.expect(
                    step["expect_prompt"],
                    timeout=step["timeout_sec"],
                )
                self.sendline(
                    step["send_input"],
                    redact=step.get("is_secret", False),
                )
            output = self.collect_remaining(timeout=final_timeout)
            return True, output
        except PromptTimeout as exc:
            return False, str(exc)

    # -- Internals ----------------------------------------------------------

    def _read_chunk(self) -> str:
        try:
            if self.channel.recv_ready():
                return self.channel.recv(4096).decode("utf-8", errors="replace")
        except Exception:
            pass
        return ""

    def _drain(self, timeout: float) -> None:
        deadline = time.monotonic() + timeout
        while time.monotonic() < deadline:
            chunk = self._read_chunk()
            if chunk:
                self.buffer += chunk
                self.full_output += chunk
            else:
                time.sleep(0.1)

    @staticmethod
    def _resolve_env(text: str) -> str:
        return re.sub(
            r'\$ENV\{(\w+)\}',
            lambda m: os.environ.get(m.group(1), f"<MISSING:{m.group(1)}>"),
            text,
        )


# ---------------------------------------------------------------------------
# MockChannel — for unit testing without hardware
# ---------------------------------------------------------------------------

class MockChannel:
    """
    Simulates a paramiko shell channel with scripted output.

    Usage::

        script = [
            (0.5, "Enter current password: "),
            (1.5, "Enter new password: "),
            (2.5, "Confirm new password: "),
            (3.5, "Password changed successfully.\\n"),
        ]
        mock_client = MockSSHClient(script)
        runner = InteractiveCommandRunner(mock_client, banner_timeout=0.1)
        ok, output = runner.run_steps(
            "ipmcset -t user -d password -v testuser",
            [
                {"expect_prompt": "current password", "send_input": "Old", "is_secret": True, "timeout_sec": 5},
                {"expect_prompt": "new password",     "send_input": "New", "is_secret": True, "timeout_sec": 5},
                {"expect_prompt": "confirm",          "send_input": "New", "is_secret": True, "timeout_sec": 5},
            ],
        )
        assert ok and "successfully" in output
    """

    def __init__(self, script: list[tuple[float, str]]):
        self._script = list(script)
        self._start = time.monotonic()
        self._pending = ""
        self.sent: list[bytes] = []
        self._closed = False

    def settimeout(self, _t): pass

    def recv_ready(self) -> bool:
        self._advance()
        return bool(self._pending)

    def recv(self, bufsize: int) -> bytes:
        self._advance()
        data = self._pending[:bufsize]
        self._pending = self._pending[bufsize:]
        return data.encode("utf-8")

    def send(self, data) -> int:
        if isinstance(data, str):
            data = data.encode("utf-8")
        self.sent.append(data)
        return len(data)

    def close(self):
        self._closed = True

    def _advance(self):
        elapsed = time.monotonic() - self._start
        ready = [(t, txt) for t, txt in self._script if t <= elapsed]
        for item in ready:
            self._pending += item[1]
            self._script.remove(item)


class MockSSHClient:
    """Wraps MockChannel to be passed to InteractiveCommandRunner."""
    def __init__(self, script: list[tuple[float, str]]):
        self._script = script
    def invoke_shell(self, **_kw) -> MockChannel:
        return MockChannel(self._script)


# ---------------------------------------------------------------------------
# Self-Test
# ---------------------------------------------------------------------------

def _self_test():
    """Smoke test — password change + secret redaction via MockChannel."""
    script = [
        (0.5, "Enter current password: "),
        (1.5, "Enter new password: "),
        (2.5, "Confirm new password: "),
        (3.5, "Password changed successfully.\n"),
    ]
    mock = MockSSHClient(script)
    runner = InteractiveCommandRunner(mock, banner_timeout=0.1)
    ok, output = runner.run_steps(
        "ipmcset -t user -d password -v testuser",
        [
            {"expect_prompt": "current password", "send_input": "OldPass", "is_secret": True, "timeout_sec": 5},
            {"expect_prompt": "new password",     "send_input": "NewPass", "is_secret": True, "timeout_sec": 5},
            {"expect_prompt": "confirm",          "send_input": "NewPass", "is_secret": True, "timeout_sec": 5},
        ],
    )
    runner.close()
    assert ok, f"Expected success, got: {output}"
    assert "successfully" in output, f"Missing 'successfully' in: {output}"

    # Verify secret redaction
    redacted = runner.redactor.redact("Password is OldPass and NewPass")
    assert "OldPass" not in redacted, f"Secret not redacted: {redacted}"
    assert "NewPass" not in redacted, f"Secret not redacted: {redacted}"
    assert "***" in redacted

    print("SELF-TEST PASSED")
    print(f"  Output: {output!r}")
    print(f"  Redaction: {redacted!r}")


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format="%(levelname)s %(message)s")
    _self_test()
