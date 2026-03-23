"""
BMC Agent Stream Parser — DeltaAccumulator (brace-counting) + InteractiveSession state machine.

Parses Claude CLI's stream-json stdout into structured BMC action objects.
Uses brace-depth counting to handle arbitrary UTF-8 delta fragments that may
split mid-JSON-object, mid-key, or even mid-codepoint.
"""

from __future__ import annotations

import enum
import json
import logging
import os
import re
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Generator, Optional

logger = logging.getLogger(__name__)

STRUCTURED_TYPES = frozenset({
    "command_plan",
    "interactive_command_plan",
    "health_check_request",
    "repair_action",
    "completion_summary",
    "error",
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
# DeltaAccumulator (brace-counting)
# ---------------------------------------------------------------------------

class DeltaAccumulator:
    """
    Accumulates ``text_delta`` fragments from Claude's ``stream-json`` output
    and extracts complete JSON objects using brace-depth counting.

    Why brace counting instead of newline splitting?
    -------------------------------------------------
    Claude's ``text_delta`` fragments split at **arbitrary** byte boundaries.
    A single JSON object may arrive across many deltas::

        delta 1: '{"type":"comman'
        delta 2: 'd_plan","id":"cm'
        delta 3: 'd_001",...}\\n{"ty'
        delta 4: 'pe":"health_check...'

    Naive ``splitlines()`` on each delta yields broken JSON.  Brace counting
    tracks ``{`` / ``}`` depth (respecting quoted strings and escapes) to find
    exact object boundaries regardless of fragment alignment.
    """

    def __init__(self) -> None:
        self._buffer: str = ""
        self._scan_pos: int = 0

    def feed(self, text_fragment: str) -> None:
        """Append a ``text_delta`` fragment to the internal buffer."""
        self._buffer += text_fragment

    def extract_actions(self) -> list[dict]:
        """
        Scan the buffer for complete JSON objects using brace-depth counting.
        Returns validated action dicts.  Incomplete trailing objects remain
        buffered for the next call.
        """
        actions: list[dict] = []
        buf = self._buffer
        i = self._scan_pos

        while i < len(buf):
            # Skip whitespace between objects
            if buf[i] in (" ", "\t", "\n", "\r"):
                i += 1
                continue

            # Look for start of JSON object
            if buf[i] != "{":
                nl = buf.find("\n", i)
                if nl == -1:
                    break  # incomplete non-JSON line — wait for more
                i = nl + 1
                continue

            # Found '{' — use brace counting to find the matching '}'
            obj_end = self._find_object_end(buf, i)
            if obj_end is None:
                break  # incomplete object — wait for more data

            candidate = buf[i:obj_end]
            i = obj_end

            try:
                obj = json.loads(candidate)
            except json.JSONDecodeError:
                # Malformed — skip to next line
                nl = buf.find("\n", i)
                i = (nl + 1) if nl != -1 else i
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

        self._scan_pos = i

        # Trim consumed buffer to prevent unbounded growth
        if self._scan_pos > 4096:
            self._buffer = self._buffer[self._scan_pos:]
            self._scan_pos = 0

        return actions

    def flush(self) -> list[dict]:
        """Final extraction — append newline to force-terminate trailing data."""
        self._buffer += "\n"
        return self.extract_actions()

    @staticmethod
    def _find_object_end(buf: str, start: int) -> Optional[int]:
        """
        Starting at buf[start] == '{', find index AFTER the matching '}'.
        Correctly handles:
          - Nested objects: {"a": {"b": 1}}
          - Strings with braces: {"msg": "use {x}"}
          - Escaped quotes: {"path": "C:\\\\Users\\\\"}
        Returns None if the object is incomplete.
        """
        depth = 0
        in_string = False
        escape = False
        i = start

        while i < len(buf):
            ch = buf[i]

            if escape:
                escape = False
                i += 1
                continue

            if ch == "\\" and in_string:
                escape = True
                i += 1
                continue

            if ch == '"':
                in_string = not in_string
            elif not in_string:
                if ch == "{":
                    depth += 1
                elif ch == "}":
                    depth -= 1
                    if depth == 0:
                        return i + 1

            i += 1

        return None  # incomplete


# ---------------------------------------------------------------------------
# Stream-JSON envelope parser (generator)
# ---------------------------------------------------------------------------

def parse_stream_lines(
    line_iterator,
) -> Generator[dict, None, None]:
    """
    Consume raw lines from Claude CLI ``--output-format stream-json`` stdout
    and yield validated structured action dicts.

    Usage::

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

        # Extract text_delta fragments
        if (
            envelope.get("type") == "content_block_delta"
            and isinstance(envelope.get("delta"), dict)
            and envelope["delta"].get("type") == "text_delta"
        ):
            acc.feed(envelope["delta"].get("text", ""))

        yield from acc.extract_actions()

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

    State transitions::

        SEND_INITIAL ──► WAITING_PROMPT ──► SENDING_INPUT ──┐
                              ▲                              │
                              └──────────────────────────────┘
                                    (next step)
                         WAITING_PROMPT (no more steps) ──► COLLECTING_TAIL ──► DONE

    On timeout: ──► TIMEOUT.
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

    def run(self) -> tuple[bool, str]:
        """Execute the state machine. Returns (success, output_or_error)."""
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
        if pattern.lower() in buf.lower():
            return True
        try:
            return bool(re.search(pattern, buf, re.IGNORECASE))
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
