"""
Interactive SSH command executor with pexpect-style API.

Built on paramiko's ``invoke_shell()`` — provides ``sendline()``,
``expect()``, ``collect_remaining()`` for driving multi-step prompts
(password changes, confirmations, menus).

Includes ``MockChannel`` for unit testing without real hardware.
"""

from __future__ import annotations

import logging
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
# InteractiveCommandRunner
# ---------------------------------------------------------------------------

class InteractiveCommandRunner:
    """
    Pexpect-like wrapper over a paramiko shell channel.

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
        self._expect_scan_pos: int = 0  # tracks where next expect() should start scanning
        # Drain the login banner so it doesn't pollute prompt matching.
        self._drain(banner_timeout)
        self._expect_scan_pos = len(self.buffer)  # skip banner

    # -- Core API ------------------------------------------------------------

    def sendline(self, text: str, redact: bool = False) -> None:
        """Send a line of text (appends ``\\n`` automatically)."""
        display = "***" if redact else text
        logger.debug("SEND: %s", display)
        self.channel.send((text + "\n").encode("utf-8"))

    def expect(self, pattern: str, timeout: float = 10.0) -> str:
        """
        Block until *pattern* appears in newly received output.

        Parameters
        ----------
        pattern
            A literal substring **or** a regular expression.  Substring
            matching is tried first (cheaper).  Regex is used as fallback.
        timeout
            Seconds to wait before raising ``PromptTimeout``.

        Returns
        -------
        str
            The full buffer contents (including history) at the point of match.

        Raises
        ------
        PromptTimeout
            If *pattern* is not found within *timeout* seconds.
        """
        deadline = time.monotonic() + timeout
        scan_start = self._expect_scan_pos

        while time.monotonic() < deadline:
            chunk = self._read_chunk()
            if chunk:
                self.buffer += chunk
                self.full_output += chunk

            new_region = self.buffer[scan_start:]

            # Substring match (case-insensitive)
            if pattern.lower() in new_region.lower():
                logger.debug("MATCH (substring): %r", pattern)
                match_idx = new_region.lower().index(pattern.lower())
                self._expect_scan_pos = scan_start + match_idx + len(pattern)
                return self.buffer

            # Regex fallback (case-insensitive)
            try:
                m = re.search(pattern, new_region, re.IGNORECASE)
                if m:
                    logger.debug("MATCH (regex): %r", pattern)
                    self._expect_scan_pos = scan_start + m.end()
                    return self.buffer
            except re.error:
                pass  # not a valid regex — substring was the only check

            time.sleep(0.05)

        raise PromptTimeout(
            f"Timeout after {timeout:.1f}s waiting for {pattern!r}.  "
            f"Buffer tail (last 300 chars): …{self.buffer[-300:]}"
        )

    def collect_remaining(self, timeout: float = 3.0) -> str:
        """Drain output for *timeout* seconds, then return ``full_output``."""
        self._drain(timeout)
        return self.full_output

    def close(self) -> None:
        """Close the underlying shell channel."""
        try:
            self.channel.close()
        except Exception:
            pass

    # -- Convenience: run a full interactive plan ----------------------------

    def run_steps(
        self,
        initial_command: str,
        steps: list[dict],
        final_timeout: float = 3.0,
    ) -> tuple[bool, str]:
        """
        Execute *initial_command*, then walk through *steps* (expect/send pairs).

        Parameters
        ----------
        initial_command
            The command that starts the interactive session.
        steps
            List of dicts, each with ``expect_prompt``, ``send_input``,
            optional ``is_secret`` (bool), optional ``timeout_seconds`` (int).
        final_timeout
            How long to drain output after the last step.

        Returns
        -------
        (success, output)
            On ``PromptTimeout``, returns ``(False, error_message)``.
        """
        try:
            self.sendline(initial_command)
            for step in steps:
                self.expect(
                    step["expect_prompt"],
                    timeout=step.get("timeout_seconds", 10),
                )
                self.sendline(
                    step["send_input"],
                    redact=step.get("is_secret", False),
                )
            output = self.collect_remaining(timeout=final_timeout)
            return True, output
        except PromptTimeout as exc:
            return False, str(exc)

    # -- Internals -----------------------------------------------------------

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


# ---------------------------------------------------------------------------
# MockChannel — for unit testing without hardware
# ---------------------------------------------------------------------------

class MockChannel:
    """
    Simulates a paramiko shell channel that plays back a scripted sequence
    of output chunks at specified delays.

    Usage::

        script = [
            (0.3, "Enter current password: "),
            (0.8, "Enter new password: "),
            (1.3, "Confirm new password: "),
            (1.8, "Password changed successfully.\\n"),
        ]
        mock_client = MockSSHClient(script)
        runner = InteractiveCommandRunner(mock_client)
        ok, output = runner.run_steps(
            "ipmcset -t user -d password -v testuser",
            [
                {"expect_prompt": "current password", "send_input": "old", "is_secret": True},
                {"expect_prompt": "new password",     "send_input": "new", "is_secret": True},
                {"expect_prompt": "confirm",          "send_input": "new", "is_secret": True},
            ],
        )
        assert ok
        assert "successfully" in output
    """

    def __init__(self, script: list[tuple[float, str]]) -> None:
        self._script: list[tuple[float, str]] = list(script)
        self._start: float = time.monotonic()
        self._pending: str = ""
        self.sent: list[bytes] = []
        self._closed = False

    # -- paramiko channel interface ------------------------------------------

    def settimeout(self, _t: float) -> None:
        pass

    def recv_ready(self) -> bool:
        self._advance()
        return bool(self._pending)

    def recv(self, bufsize: int) -> bytes:
        self._advance()
        data = self._pending[:bufsize]
        self._pending = self._pending[bufsize:]
        return data.encode("utf-8")

    def send(self, data: bytes | str) -> int:
        if isinstance(data, str):
            data = data.encode("utf-8")
        self.sent.append(data)
        return len(data)

    def close(self) -> None:
        self._closed = True

    # -- internal ------------------------------------------------------------

    def _advance(self) -> None:
        elapsed = time.monotonic() - self._start
        ready = [(t, txt) for t, txt in self._script if t <= elapsed]
        for item in ready:
            self._pending += item[1]
            self._script.remove(item)


class MockSSHClient:
    """Wraps a MockChannel so it can be passed to ``InteractiveCommandRunner``."""

    def __init__(self, script: list[tuple[float, str]]) -> None:
        self._script = script

    def invoke_shell(self, **_kw) -> MockChannel:
        return MockChannel(self._script)


# ---------------------------------------------------------------------------
# Self-test
# ---------------------------------------------------------------------------

def _self_test() -> None:
    """Quick smoke test using MockChannel — no hardware needed."""
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
            {"expect_prompt": "current password", "send_input": "OldPass", "is_secret": True, "timeout_seconds": 5},
            {"expect_prompt": "new password",     "send_input": "NewPass", "is_secret": True, "timeout_seconds": 5},
            {"expect_prompt": "confirm",          "send_input": "NewPass", "is_secret": True, "timeout_seconds": 5},
        ],
    )
    runner.close()
    assert ok, f"Expected success, got: {output}"
    assert "successfully" in output, f"Missing 'successfully' in: {output}"
    print("SELF-TEST PASSED")
    print(f"  Output: {output!r}")
    print(f"  Sent:   {[s.decode() for s in runner.channel.sent]}")


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format="%(levelname)s %(message)s")
    _self_test()
