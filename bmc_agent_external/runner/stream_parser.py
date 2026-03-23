"""
BMC Agent Stream Parser — DeltaAccumulator + InteractiveSession state machine.

Parses Claude CLI's stream-json stdout into structured BMC action objects.
Handles arbitrary UTF-8 delta fragments correctly (no naive line splitting).
"""

from __future__ import annotations

import enum
import json
import logging
import os
import re
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Generator, Optional

logger = logging.getLogger(__name__)

STRUCTURED_TYPES = frozenset({
    "command_plan",
    "interactive_command_plan",
    "health_check_request",
    "repair_action",
    "completion_summary",
})

# Optional: load JSON Schema for validation
_SCHEMA: Optional[dict] = None
try:
    import jsonschema

    _schema_path = Path(__file__).resolve().parent.parent / "schemas" / "bmc_action_schemas.json"
    if _schema_path.exists():
        with open(_schema_path) as f:
            _SCHEMA = json.load(f)
        logger.info("Loaded action schema from %s", _schema_path)
except ImportError:
    jsonschema = None  # type: ignore[assignment]


# ---------------------------------------------------------------------------
# DeltaAccumulator
# ---------------------------------------------------------------------------

class DeltaAccumulator:
    """
    Accumulates ``text_delta`` fragments from Claude's ``stream-json`` output
    and yields complete, validated structured-action dicts.

    Why this exists
    ---------------
    Claude's ``stream-json`` format emits events like::

        {"type":"content_block_delta","index":0,
         "delta":{"type":"text_delta","text":"<fragment>"}}

    The ``<fragment>`` is an **arbitrary** UTF-8 slice — it may be a single
    character, half a JSON key, or three complete JSON lines glued together.
    Splitting on ``\\n`` naively would yield broken JSON.

    This class buffers text and only attempts JSON parsing on fully
    newline-terminated lines.  A trailing non-terminated fragment is kept in
    the buffer for the next ``feed()`` call.
    """

    def __init__(self) -> None:
        self._buffer: str = ""
        self._scan_pos: int = 0  # up to where we've consumed complete lines

    # -- public API ----------------------------------------------------------

    def feed(self, text_fragment: str) -> None:
        """Append a ``text_delta`` fragment to the internal buffer."""
        self._buffer += text_fragment

    def extract_actions(self) -> list[dict]:
        """
        Scan the buffer for new complete lines that parse as structured actions.

        A "complete line" = text terminated by ``\\n``.  Unterminated trailing
        text is left in the buffer because the next delta may complete it.
        """
        last_nl = self._buffer.rfind("\n", self._scan_pos)
        if last_nl < self._scan_pos:
            return []  # no new complete lines

        region = self._buffer[self._scan_pos : last_nl + 1]
        self._scan_pos = last_nl + 1

        return self._parse_region(region)

    def flush(self) -> list[dict]:
        """Force-parse any remaining unterminated text (call at stream end)."""
        if self._scan_pos < len(self._buffer):
            self._buffer += "\n"
            return self.extract_actions()
        return []

    # -- internals -----------------------------------------------------------

    @staticmethod
    def _parse_region(region: str) -> list[dict]:
        actions: list[dict] = []
        for line in region.splitlines():
            line = line.strip()
            if not line or line[0] != "{":
                continue
            try:
                obj = json.loads(line)
            except json.JSONDecodeError:
                continue

            if not isinstance(obj, dict):
                continue
            obj_type = obj.get("type")
            if obj_type not in STRUCTURED_TYPES:
                continue

            # Optional schema validation
            if _SCHEMA is not None and jsonschema is not None:
                try:
                    jsonschema.validate(obj, _SCHEMA)
                except jsonschema.ValidationError as exc:
                    logger.warning(
                        "Schema validation failed for %s/%s: %s",
                        obj_type, obj.get("id", "?"), exc.message,
                    )
                    continue

            actions.append(obj)
        return actions


# ---------------------------------------------------------------------------
# Stream-JSON envelope parser (generator)
# ---------------------------------------------------------------------------

def parse_stream_lines(
    line_iterator,
) -> Generator[dict, None, None]:
    """
    Consume raw lines from Claude CLI's ``--output-format stream-json`` stdout
    and yield validated structured action dicts.

    Parameters
    ----------
    line_iterator
        Iterable of raw ``str`` lines (e.g. ``process.stdout``).

    Yields
    ------
    dict
        Each dict is a validated action with a ``type`` field in
        ``STRUCTURED_TYPES``.

    Example
    -------
    ::

        process = subprocess.Popen(
            ["claude", "-p", prompt, "--output-format", "stream-json"],
            stdout=subprocess.PIPE, text=True, bufsize=1,
        )
        for action in parse_stream_lines(process.stdout):
            handle(action)
    """
    acc = DeltaAccumulator()

    for raw_line in line_iterator:
        raw_line = raw_line.rstrip("\n\r")
        if not raw_line:
            continue

        try:
            envelope = json.loads(raw_line)
        except json.JSONDecodeError:
            continue

        # Extract text_delta fragments from content_block_delta events.
        if (
            envelope.get("type") == "content_block_delta"
            and isinstance(envelope.get("delta"), dict)
            and envelope["delta"].get("type") == "text_delta"
        ):
            acc.feed(envelope["delta"].get("text", ""))

        yield from acc.extract_actions()

    # Final flush for any unterminated trailing text.
    yield from acc.flush()


# ---------------------------------------------------------------------------
# InteractiveSession state machine
# ---------------------------------------------------------------------------

class _State(enum.Enum):
    SEND_INITIAL    = "send_initial"
    WAITING_PROMPT  = "waiting_prompt"
    SENDING_INPUT   = "sending_input"
    COLLECTING_TAIL = "collecting_tail"
    DONE            = "done"
    TIMEOUT         = "timeout"
    ERROR           = "error"


class InteractiveSession:
    """
    State-machine driver for interactive (prompt/response) command sequences.

    Designed to run on top of a paramiko shell channel but decoupled enough
    to work with any object that supports ``.send(bytes)``, ``.recv(int)``,
    and ``.recv_ready() -> bool``.

    State transitions::

        SEND_INITIAL ──► WAITING_PROMPT ──► SENDING_INPUT ──┐
                              ▲                              │
                              └──────────────────────────────┘
                                    (next step)
                         WAITING_PROMPT (no more steps) ──► COLLECTING_TAIL ──► DONE

    On timeout at any point: ──► TIMEOUT.
    """

    TAIL_DRAIN_SECONDS = 2.0

    def __init__(
        self,
        channel,
        initial_command: str,
        steps: list[dict],
        total_timeout: float = 60.0,
    ) -> None:
        self.channel = channel
        self.initial_command = initial_command
        self.steps = steps
        self.total_timeout = total_timeout

        self.state = _State.SEND_INITIAL
        self.step_idx = 0
        self.output = ""
        self._step_buf = ""
        self._deadline = time.monotonic() + total_timeout
        self.error_message = ""

    # -- public --------------------------------------------------------------

    def run(self) -> tuple[bool, str]:
        """
        Execute the state machine to completion.

        Returns
        -------
        (success, output_or_error)
            ``success`` is True when all steps completed and state reached DONE.
            ``output_or_error`` is the accumulated terminal output on success,
            or the error/timeout message on failure.
        """
        terminal = {_State.DONE, _State.TIMEOUT, _State.ERROR}
        while self.state not in terminal:
            if time.monotonic() > self._deadline:
                self.state = _State.TIMEOUT
                self.error_message = (
                    f"Global timeout ({self.total_timeout}s) at step "
                    f"{self.step_idx + 1}/{len(self.steps)}"
                )
                break
            self._tick()

        ok = self.state is _State.DONE
        return ok, self.output if ok else (self.error_message or f"State: {self.state.value}")

    # -- state handlers ------------------------------------------------------

    def _tick(self) -> None:
        if self.state is _State.SEND_INITIAL:
            self._send(self.initial_command + "\n")
            self._step_buf = ""
            self.state = _State.WAITING_PROMPT

        elif self.state is _State.WAITING_PROMPT:
            chunk = self._recv()
            if chunk:
                self._step_buf += chunk
                self.output += chunk

            if self.step_idx >= len(self.steps):
                self.state = _State.COLLECTING_TAIL
                return

            step = self.steps[self.step_idx]
            if self._prompt_matches(self._step_buf, step["expect_prompt"]):
                self.state = _State.SENDING_INPUT

        elif self.state is _State.SENDING_INPUT:
            step = self.steps[self.step_idx]
            text = _resolve_env(step["send_input"])
            self._send(text + "\n")
            self.step_idx += 1
            self._step_buf = ""
            self.state = _State.WAITING_PROMPT

        elif self.state is _State.COLLECTING_TAIL:
            tail_end = min(time.monotonic() + self.TAIL_DRAIN_SECONDS, self._deadline)
            while time.monotonic() < tail_end:
                chunk = self._recv()
                if chunk:
                    self.output += chunk
                else:
                    time.sleep(0.05)
            self.state = _State.DONE

    # -- I/O helpers ---------------------------------------------------------

    def _send(self, data: str) -> None:
        self.channel.send(data.encode("utf-8") if isinstance(data, str) else data)

    def _recv(self) -> str:
        try:
            if self.channel.recv_ready():
                return self.channel.recv(4096).decode("utf-8", errors="replace")
        except Exception:
            pass
        time.sleep(0.05)
        return ""

    @staticmethod
    def _prompt_matches(buf: str, pattern: str) -> bool:
        if pattern in buf:
            return True
        try:
            return bool(re.search(pattern, buf))
        except re.error:
            return False


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _resolve_env(text: str) -> str:
    """Replace ``$ENV{VAR}`` placeholders with ``os.environ`` values."""
    return re.sub(
        r"\$ENV\{(\w+)\}",
        lambda m: os.environ.get(m.group(1), f"<MISSING:{m.group(1)}>"),
        text,
    )


# ---------------------------------------------------------------------------
# StepResult dataclass (used by runners)
# ---------------------------------------------------------------------------

@dataclass
class StepResult:
    """Result of executing a single action."""
    id: str
    status: str  # "pass" | "fail" | "error"
    note: str = ""
    stdout: str = ""
    stderr: str = ""
