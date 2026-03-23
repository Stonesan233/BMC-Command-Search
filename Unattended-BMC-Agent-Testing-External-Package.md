# Unattended BMC Agent Testing — External Implementation Package

> **Version**: 1.1 | **Date**: 2026-03-23
> **Scope**: Everything you can build and validate without access to the closed-source internal test framework. Copy-paste ready.

---

## Table of Contents

1. [Agent System Prompt (CLAUDE.md)](#1-agent-system-prompt)
2. [Structured JSON Schemas](#2-structured-json-schemas)
3. [Test Runner Pseudo-Code](#3-test-runner-pseudo-code)
4. [ssh.py Enhancement Suggestions](#4-sshpy-enhancement-suggestions)

---

## 1. Agent System Prompt

Place the content below in `CLAUDE.md` at the project root. Claude Code reads this file automatically on every invocation.

````markdown
# BMC Unattended Test Agent

You are an automated BMC (Baseboard Management Controller) test execution agent.
You receive a test case definition and produce **structured JSON actions** that a
test runner will execute against real hardware. You never execute commands yourself.

## Output Contract

- Every line you output MUST be a single, self-contained JSON object.
- No markdown fences, no prose, no commentary — **only JSON lines**.
- Each JSON object MUST contain a `"type"` field as discriminator.
- End every test case with exactly ONE `completion_summary`.

### Valid `type` values

| type                       | When to use                                                  |
|----------------------------|--------------------------------------------------------------|
| `command_plan`             | Non-interactive commands (run → exit code → done)            |
| `interactive_command_plan` | Commands with prompts: passwords, confirmations, menus       |
| `health_check_request`     | Pre/post verification of environment state                   |
| `repair_action`            | Fix a detected issue before retrying                         |
| `completion_summary`       | Final verdict — exactly once, always last                    |

## Command Allowlist

You may ONLY emit commands whose first token starts with one of:

- `ipmcget` — query BMC state
- `ipmcset` — modify BMC configuration
- `ipmitool` — IPMI raw/standard commands
- `curl` — Redfish REST API calls only (target must be BMC Redfish endpoint)
- `snmpget` — SNMP single OID query
- `snmpwalk` — SNMP subtree walk

**If the test case requires a command not in this allowlist**, do NOT emit a command_plan
or interactive_command_plan. Instead emit:

```
{"type":"error","reason":"command not allowed","attempted_command":"<the command>","suggestion":"<alternative using allowed commands>"}
```

The runner will log this and skip the step.

## Decision Rules

1. **BEFORE any credential or destructive operation** → emit `health_check_request`.
2. **If a command has ANY interactive prompt** → use `interactive_command_plan`, NEVER `command_plan`.
3. **Every step in `interactive_command_plan` MUST include `timeout_sec`** — there is no default. Typical values: 10 for password prompts, 30 for firmware operations, 5 for yes/no confirmations.
4. **If a health check fails** → emit `repair_action`, then retry. Max 3 repair cycles total.
5. **Phase ordering is mandatory**: `precondition` → `execute` → `postcondition`. Never skip.
6. **After changes, always verify** with a postcondition health check.
7. **Passwords and secrets**: use `$ENV{VAR_NAME}` placeholders. Mark steps `"is_secret": true`.

## MCP Tool Usage

You have access to the `bmc_commands_search` MCP server. Use it to look up exact
command syntax before emitting any `command_plan` or `interactive_command_plan`.
Search by keyword (e.g., "user password", "fan speed", "firmware version").
Use the returned command details (syntax, parameters, expected output format) to
build accurate plans.

---

## Inline Examples

### Example 1: Simple non-interactive query

```
{"type":"command_plan","id":"cmd_001","phase":"precondition","description":"Verify BMC is reachable","target":{"host":"{{TARGET_HOST}}","port":22,"protocol":"ssh"},"command":"ipmcget -d deviceinfo","timeout_seconds":15,"expected_exit_code":0,"expected_output_contains":["Board ID"],"on_failure":"abort"}
```

### Example 2: Interactive password change (note: every step has timeout_sec)

```
{"type":"interactive_command_plan","id":"icmd_001","phase":"execute","description":"Change testuser password","target":{"host":"{{TARGET_HOST}}","port":22,"protocol":"ssh"},"initial_command":"ipmcset -t user -d password -v testuser","timeout_seconds":60,"steps":[{"step":1,"expect_prompt":"current password","send_input":"$ENV{OLD_PASSWORD}","is_secret":true,"timeout_sec":10},{"step":2,"expect_prompt":"new password","send_input":"$ENV{NEW_PASSWORD}","is_secret":true,"timeout_sec":10},{"step":3,"expect_prompt":"confirm","send_input":"$ENV{NEW_PASSWORD}","is_secret":true,"timeout_sec":10}],"expected_final_output_contains":["success"],"on_failure":"repair"}
```

### Example 3: Health check with multiple sub-checks

```
{"type":"health_check_request","id":"hc_001","phase":"precondition","description":"Verify user state before password change","target":{"host":"{{TARGET_HOST}}","port":22,"protocol":"ssh"},"checks":[{"name":"user_exists","command":"ipmcget -d userlist","expect_output_contains":["testuser"],"timeout_seconds":10},{"name":"user_enabled","command":"ipmcget -t user -d state -v testuser","expect_output_contains":["Enabled"],"timeout_seconds":10}],"on_any_failure":"repair"}
```

### Example 4: Repair action

```
{"type":"repair_action","id":"fix_001","issue":"User testuser is locked","severity":"critical","target":{"host":"{{TARGET_HOST}}","port":22,"protocol":"ssh"},"repair_commands":[{"command":"ipmcset -t user -d unlock -v testuser","timeout_seconds":15,"expected_exit_code":0}],"verify_after_repair":true,"on_repair_failure":"abort"}
```

### Example 5: Completion summary with context passing

```
{"type":"completion_summary","test_case":"TC_USER_PASSWORD_CHANGE_001","status":"pass","steps_executed":5,"steps_passed":5,"steps_failed":0,"repairs_attempted":0,"repairs_succeeded":0,"duration_hint_seconds":35,"summary":"Password changed successfully. User enabled.","details":[{"id":"hc_001","status":"pass","note":"Preconditions met"},{"id":"cmd_001","status":"pass","note":"User verified"},{"id":"icmd_001","status":"pass","note":"Password changed"},{"id":"hc_002","status":"pass","note":"Postconditions met"}],"failed_step_id":null,"error_details":null,"next_context_summary":"Password for testuser changed from OldPass to NewPass. User is enabled. BMC firmware V5.05.00.12."}
```

### Example 6: Completion summary on failure (note failed_step_id)

```
{"type":"completion_summary","test_case":"TC_USER_PASSWORD_CHANGE_001","status":"fail","steps_executed":3,"steps_passed":2,"steps_failed":1,"repairs_attempted":1,"repairs_succeeded":0,"duration_hint_seconds":28,"summary":"Password change failed at confirm prompt.","details":[{"id":"hc_001","status":"pass","note":"Preconditions met"},{"id":"icmd_001","status":"fail","note":"Timeout at step 3"}],"failed_step_id":"icmd_001.step3","error_details":{"failed_step_id":"icmd_001.step3","error_type":"prompt_timeout","message":"Timed out waiting for confirm prompt after 10s","stdout_tail":"Enter new password: ","stderr_tail":""},"next_context_summary":"Password change FAILED. Original password still active. User testuser is enabled."}
```

### Example 7: Command not in allowlist

```
{"type":"error","reason":"command not allowed","attempted_command":"rm -rf /tmp/bmc_logs","suggestion":"Use ipmcget -d loginfo to query logs instead of filesystem operations"}
```

## Critical Constraints

- **No shell metacharacters**: Never use `$()`, backticks, pipes, or redirects in command fields. The runner calls `exec_command()` directly (no shell expansion).
- **Secrets**: Use `$ENV{VAR_NAME}` placeholders for passwords/tokens. The runner resolves these at runtime. Mark steps containing secrets with `"is_secret": true`.
- **One JSON per line**: Partial JSON or multi-line JSON will be silently dropped.
- **Redfish via curl**: When using `curl` for Redfish, always include `-k` (skip TLS verify for BMC self-signed certs) and use `$ENV{BMC_TOKEN}` for auth headers.
````

---

## 2. Structured JSON Schemas

All schemas below use [JSON Schema Draft 2020-12](https://json-schema.org/draft/2020-12/schema) conventions. The runner validates every extracted JSON object against these before execution.

### 2.1 `command_plan`

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "command_plan",
  "type": "object",
  "required": ["type", "id", "phase", "description", "target", "command", "timeout_seconds", "on_failure"],
  "additionalProperties": false,
  "properties": {
    "type":                     { "const": "command_plan" },
    "id":                       { "type": "string", "pattern": "^cmd_[0-9]{3,}$" },
    "phase":                    { "type": "string", "enum": ["precondition", "execute", "postcondition"] },
    "description":              { "type": "string", "minLength": 5 },
    "target": {
      "type": "object",
      "required": ["host", "port", "protocol"],
      "properties": {
        "host":     { "type": "string" },
        "port":     { "type": "integer", "default": 22 },
        "protocol": { "type": "string", "enum": ["ssh"] }
      },
      "additionalProperties": false
    },
    "command":                  { "type": "string", "minLength": 1 },
    "timeout_seconds":         { "type": "integer", "minimum": 1, "maximum": 300 },
    "expected_exit_code":      { "type": "integer", "default": 0 },
    "expected_output_contains": { "type": "array", "items": { "type": "string" }, "default": [] },
    "on_failure":              { "type": "string", "enum": ["abort", "continue", "retry", "repair"] }
  }
}
```

### 2.2 `interactive_command_plan`

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "interactive_command_plan",
  "type": "object",
  "required": ["type", "id", "phase", "description", "target", "initial_command", "timeout_seconds", "steps", "on_failure"],
  "additionalProperties": false,
  "properties": {
    "type":              { "const": "interactive_command_plan" },
    "id":                { "type": "string", "pattern": "^icmd_[0-9]{3,}$" },
    "phase":             { "type": "string", "enum": ["precondition", "execute", "postcondition"] },
    "description":       { "type": "string", "minLength": 5 },
    "target": {
      "type": "object",
      "required": ["host", "port", "protocol"],
      "properties": {
        "host":     { "type": "string" },
        "port":     { "type": "integer", "default": 22 },
        "protocol": { "type": "string", "enum": ["ssh"] }
      },
      "additionalProperties": false
    },
    "initial_command":   { "type": "string", "minLength": 1 },
    "timeout_seconds":   { "type": "integer", "minimum": 1, "maximum": 600 },
    "steps": {
      "type": "array",
      "minItems": 1,
      "items": {
        "type": "object",
        "required": ["step", "expect_prompt", "send_input", "timeout_sec"],
        "additionalProperties": false,
        "properties": {
          "step":            { "type": "integer", "minimum": 1 },
          "expect_prompt":   { "type": "string", "minLength": 1 },
          "send_input":      { "type": "string" },
          "is_secret":       { "type": "boolean", "default": false },
          "timeout_sec":     { "type": "integer", "minimum": 1, "description": "Per-step timeout in seconds. Required — no default. Typical: 10 for passwords, 30 for firmware, 5 for yes/no." }
        }
      }
    },
    "expected_final_output_contains": { "type": "array", "items": { "type": "string" }, "default": [] },
    "on_failure":        { "type": "string", "enum": ["abort", "continue", "retry", "repair"] }
  }
}
```

### 2.3 `health_check_request`

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "health_check_request",
  "type": "object",
  "required": ["type", "id", "phase", "description", "target", "checks", "on_any_failure"],
  "additionalProperties": false,
  "properties": {
    "type":           { "const": "health_check_request" },
    "id":             { "type": "string", "pattern": "^hc_[0-9]{3,}$" },
    "phase":          { "type": "string", "enum": ["precondition", "postcondition"] },
    "description":    { "type": "string", "minLength": 5 },
    "target": {
      "type": "object",
      "required": ["host", "port", "protocol"],
      "properties": {
        "host":     { "type": "string" },
        "port":     { "type": "integer", "default": 22 },
        "protocol": { "type": "string", "enum": ["ssh"] }
      },
      "additionalProperties": false
    },
    "checks": {
      "type": "array",
      "minItems": 1,
      "items": {
        "type": "object",
        "required": ["name", "command"],
        "additionalProperties": false,
        "properties": {
          "name":                   { "type": "string" },
          "command":                { "type": "string" },
          "expect_output_contains": { "type": "array", "items": { "type": "string" }, "default": [] },
          "expect_exit_code":       { "type": "integer" },
          "timeout_seconds":        { "type": "integer", "minimum": 1, "default": 10 }
        }
      }
    },
    "on_any_failure":  { "type": "string", "enum": ["abort", "repair"] }
  }
}
```

### 2.4 `repair_action`

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "repair_action",
  "type": "object",
  "required": ["type", "id", "issue", "severity", "target", "repair_commands", "on_repair_failure"],
  "additionalProperties": false,
  "properties": {
    "type":                { "const": "repair_action" },
    "id":                  { "type": "string", "pattern": "^fix_[0-9]{3,}$" },
    "issue":               { "type": "string", "minLength": 5 },
    "severity":            { "type": "string", "enum": ["warning", "critical", "fatal"] },
    "target": {
      "type": "object",
      "required": ["host", "port", "protocol"],
      "properties": {
        "host":     { "type": "string" },
        "port":     { "type": "integer", "default": 22 },
        "protocol": { "type": "string", "enum": ["ssh"] }
      },
      "additionalProperties": false
    },
    "repair_commands": {
      "type": "array",
      "minItems": 1,
      "items": {
        "type": "object",
        "required": ["command"],
        "additionalProperties": false,
        "properties": {
          "command":                  { "type": "string" },
          "timeout_seconds":          { "type": "integer", "minimum": 1, "default": 15 },
          "expected_exit_code":       { "type": "integer" },
          "expected_output_contains": { "type": "array", "items": { "type": "string" }, "default": [] }
        }
      }
    },
    "verify_after_repair":  { "type": "boolean", "default": true },
    "on_repair_failure":    { "type": "string", "enum": ["abort", "continue"] }
  }
}
```

### 2.5 `completion_summary` (with `next_context_summary` and `failed_step_id`)

The `next_context_summary` field enables **cross-case context passing**. When the runner starts the next test case, it injects this string into the agent prompt as `Previous Context`.

The `failed_step_id` field pinpoints which step failed, using dot notation for sub-steps (e.g., `"icmd_001.step2"` means step 2 of interactive command icmd_001).

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "completion_summary",
  "type": "object",
  "required": ["type", "test_case", "status", "steps_executed", "steps_passed", "steps_failed",
               "repairs_attempted", "repairs_succeeded", "summary", "details"],
  "additionalProperties": false,
  "properties": {
    "type":                  { "const": "completion_summary" },
    "test_case":             { "type": "string" },
    "status":                { "type": "string", "enum": ["pass", "fail", "error"] },
    "steps_executed":        { "type": "integer", "minimum": 0 },
    "steps_passed":          { "type": "integer", "minimum": 0 },
    "steps_failed":          { "type": "integer", "minimum": 0 },
    "repairs_attempted":     { "type": "integer", "minimum": 0 },
    "repairs_succeeded":     { "type": "integer", "minimum": 0 },
    "duration_hint_seconds": { "type": "integer", "minimum": 0 },
    "summary":               { "type": "string", "minLength": 1 },
    "details": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["id", "status", "note"],
        "additionalProperties": false,
        "properties": {
          "id":     { "type": "string" },
          "status": { "type": "string", "enum": ["pass", "fail", "error", "skipped"] },
          "note":   { "type": "string" }
        }
      }
    },
    "failed_step_id": {
      "type": ["string", "null"],
      "default": null,
      "description": "Dot-notation ID of the step that caused failure. Examples: 'cmd_003' for a command_plan, 'icmd_001.step2' for step 2 of an interactive plan, 'hc_002.user_locked' for a specific health check. Null when status is 'pass'."
    },
    "error_details": {
      "oneOf": [
        {
          "type": "object",
          "required": ["failed_step_id", "error_type", "message"],
          "additionalProperties": false,
          "properties": {
            "failed_step_id": { "type": "string" },
            "error_type":     { "type": "string", "enum": ["timeout", "exit_code_mismatch", "output_mismatch", "ssh_error", "prompt_timeout", "repair_exhausted", "command_not_allowed", "unknown"] },
            "message":        { "type": "string" },
            "stdout_tail":    { "type": "string", "description": "Last 500 chars of stdout at failure." },
            "stderr_tail":    { "type": "string", "description": "Last 500 chars of stderr at failure." }
          }
        },
        { "type": "null" }
      ],
      "default": null
    },
    "next_context_summary": {
      "type": ["string", "null"],
      "default": null,
      "description": "Free-text summary of state changes for the next test case. Include: what changed, current credential state, firmware versions, any anomalies observed."
    }
  }
}
```

**Usage pattern in the runner:**

```python
# After test case N completes:
context_for_next = summary.get("next_context_summary", "")
failed_at = summary.get("failed_step_id")  # e.g. "icmd_001.step2" or None

# When building prompt for test case N+1:
prompt = build_agent_prompt(next_test_case, context=context_for_next)
```

---

## 3. Test Runner Pseudo-Code

Key improvements over the original spec:
- **Brace-counting delta accumulator**: handles UTF-8 delta fragments that split mid-JSON-object. Uses brace depth tracking instead of naive newline splitting, so a JSON object spanning multiple deltas is correctly reassembled.
- **State machine for interactive command execution**: explicit states (`SEND_INITIAL`, `WAITING_PROMPT`, `SENDING_INPUT`, `COLLECTING_TAIL`, `DONE`) instead of sleep-based polling.
- **Schema validation** before execution.
- **Cross-case context passing** via `next_context_summary`.

```python
#!/usr/bin/env python3
"""
BMC Agent-Driven Test Runner — External Implementation
Launches Claude CLI with stream-json, accumulates text deltas using
brace-counting JSON extraction, executes structured actions via SSH.
"""

import subprocess
import json
import re
import time
import enum
import logging
from dataclasses import dataclass, field
from typing import Generator, Optional

try:
    import jsonschema
    HAS_JSONSCHEMA = True
except ImportError:
    HAS_JSONSCHEMA = False

logger = logging.getLogger("bmc_runner")


# ─────────────────────────────────────────────
# 3.1  Stream-JSON Delta Accumulator (Brace-Counting)
# ─────────────────────────────────────────────

STRUCTURED_TYPES = {
    "command_plan", "interactive_command_plan",
    "health_check_request", "repair_action", "completion_summary", "error"
}

SCHEMAS: dict[str, dict] = {}  # type_name -> JSON Schema dict


class DeltaAccumulator:
    """
    Accumulates text_delta fragments from Claude's stream-json output
    and extracts complete JSON objects using brace-depth counting.

    Why brace counting?
    -------------------
    Claude's text_delta fragments split at ARBITRARY byte boundaries.
    A single JSON object may arrive across 2, 5, or 50 deltas:

        delta 1: '{"type":"comman'
        delta 2: 'd_plan","id":"cm'
        delta 3: 'd_001",...}\n{"ty'
        delta 4: 'pe":"health_check...'

    Naive newline splitting fails when a delta boundary falls inside
    a JSON object. Brace counting tracks { } depth (respecting strings)
    to find exact object boundaries regardless of how deltas fragment.
    """

    def __init__(self) -> None:
        self._buffer: str = ""
        self._scan_pos: int = 0

    def feed(self, text_fragment: str) -> None:
        """Append a text_delta fragment to the internal buffer."""
        self._buffer += text_fragment

    def extract_actions(self) -> list[dict]:
        """
        Scan the buffer for complete JSON objects using brace-depth counting.
        Handles objects split across multiple deltas and multiple objects
        within a single delta.
        """
        actions: list[dict] = []
        buf = self._buffer
        i = self._scan_pos

        while i < len(buf):
            # Skip whitespace and newlines between objects
            if buf[i] in (' ', '\t', '\n', '\r'):
                i += 1
                continue

            # Look for start of JSON object
            if buf[i] != '{':
                # Skip non-JSON text (agent commentary, if any)
                nl = buf.find('\n', i)
                if nl == -1:
                    break  # incomplete non-JSON line, wait for more data
                i = nl + 1
                continue

            # Found '{' — count braces to find matching '}'
            obj_start = i
            result = self._find_object_end(buf, obj_start)

            if result is None:
                # Incomplete JSON object — stop scanning, wait for more data
                break

            obj_end = result  # index AFTER the closing '}'
            candidate = buf[obj_start:obj_end]

            try:
                obj = json.loads(candidate)
            except json.JSONDecodeError:
                # Malformed JSON — skip to next line
                nl = buf.find('\n', obj_start)
                i = (nl + 1) if nl != -1 else obj_end
                continue

            if isinstance(obj, dict) and obj.get("type") in STRUCTURED_TYPES:
                # Optional schema validation
                if HAS_JSONSCHEMA and obj["type"] in SCHEMAS:
                    try:
                        jsonschema.validate(obj, SCHEMAS[obj["type"]])
                    except jsonschema.ValidationError as e:
                        logger.warning("Schema validation failed for %s: %s",
                                       obj.get("id", "?"), e.message)
                        i = obj_end
                        continue
                actions.append(obj)

            i = obj_end

        self._scan_pos = i

        # Trim consumed portion of buffer to prevent unbounded growth
        if self._scan_pos > 4096:
            self._buffer = self._buffer[self._scan_pos:]
            self._scan_pos = 0

        return actions

    def flush(self) -> list[dict]:
        """Final extraction — append newline to terminate any trailing data."""
        self._buffer += "\n"
        return self.extract_actions()

    @staticmethod
    def _find_object_end(buf: str, start: int) -> Optional[int]:
        """
        Starting from buf[start] == '{', find the index after the matching '}'.
        Respects JSON string literals (skips braces inside "...").
        Returns None if the object is incomplete (not enough data yet).
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

            if ch == '\\' and in_string:
                escape = True
                i += 1
                continue

            if ch == '"':
                in_string = not in_string
            elif not in_string:
                if ch == '{':
                    depth += 1
                elif ch == '}':
                    depth -= 1
                    if depth == 0:
                        return i + 1  # index after closing brace

            i += 1

        return None  # incomplete — brace not closed yet


# ─────────────────────────────────────────────
# 3.2  Stream-JSON Envelope Parser (Generator)
# ─────────────────────────────────────────────

def parse_stream_lines(line_iterator) -> Generator[dict, None, None]:
    """
    Consume raw lines from Claude CLI's --output-format stream-json stdout
    and yield validated structured action dicts.

    Usage:
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

        # Extract text_delta fragments from content_block_delta events
        if (envelope.get("type") == "content_block_delta"
                and isinstance(envelope.get("delta"), dict)
                and envelope["delta"].get("type") == "text_delta"):
            acc.feed(envelope["delta"].get("text", ""))

        yield from acc.extract_actions()

    yield from acc.flush()


# ─────────────────────────────────────────────
# 3.3  Interactive Command State Machine
# ─────────────────────────────────────────────

class InteractiveState(enum.Enum):
    SEND_INITIAL    = "send_initial"
    WAITING_PROMPT  = "waiting_prompt"
    SENDING_INPUT   = "sending_input"
    COLLECTING_TAIL = "collecting_tail"
    DONE            = "done"
    TIMEOUT         = "timeout"
    ERROR           = "error"


class InteractiveSession:
    """
    State-machine driver for interactive prompt/response sequences.

    State transitions:
        SEND_INITIAL ──► WAITING_PROMPT ──► SENDING_INPUT ──┐
                              ▲                              │
                              └──────────────────────────────┘
                                    (next step)
                         WAITING_PROMPT (no more steps) ──► COLLECTING_TAIL ──► DONE
    """

    TAIL_DRAIN_SECONDS = 2.0

    def __init__(self, channel, initial_command: str, steps: list[dict],
                 total_timeout: float = 60.0):
        self.channel = channel
        self.initial_command = initial_command
        self.steps = steps
        self.total_timeout = total_timeout
        self.state = InteractiveState.SEND_INITIAL
        self.step_idx = 0
        self.output = ""
        self._step_buf = ""
        self._deadline = time.monotonic() + total_timeout
        self.error_message = ""

    def run(self) -> tuple[bool, str]:
        """Execute the state machine. Returns (success, output_or_error)."""
        terminal = {InteractiveState.DONE, InteractiveState.TIMEOUT, InteractiveState.ERROR}
        while self.state not in terminal:
            if time.monotonic() > self._deadline:
                self.state = InteractiveState.TIMEOUT
                self.error_message = (
                    f"Global timeout ({self.total_timeout}s) at step "
                    f"{self.step_idx + 1}/{len(self.steps)}")
                break
            self._tick()
        ok = self.state is InteractiveState.DONE
        return ok, self.output if ok else (self.error_message or f"State: {self.state.value}")

    def _tick(self):
        if self.state is InteractiveState.SEND_INITIAL:
            self.channel.send(self.initial_command + "\n")
            self._step_buf = ""
            self.state = InteractiveState.WAITING_PROMPT

        elif self.state is InteractiveState.WAITING_PROMPT:
            chunk = self._recv()
            if chunk:
                self._step_buf += chunk
                self.output += chunk
            if self.step_idx >= len(self.steps):
                self.state = InteractiveState.COLLECTING_TAIL
                return
            step = self.steps[self.step_idx]
            if self._prompt_matches(self._step_buf, step["expect_prompt"]):
                self.state = InteractiveState.SENDING_INPUT

        elif self.state is InteractiveState.SENDING_INPUT:
            step = self.steps[self.step_idx]
            text = _resolve_env(step["send_input"])
            self.channel.send(text + "\n")
            self.step_idx += 1
            self._step_buf = ""
            self.state = InteractiveState.WAITING_PROMPT

        elif self.state is InteractiveState.COLLECTING_TAIL:
            tail_end = min(time.monotonic() + self.TAIL_DRAIN_SECONDS, self._deadline)
            while time.monotonic() < tail_end:
                chunk = self._recv()
                if chunk:
                    self.output += chunk
                else:
                    time.sleep(0.05)
            self.state = InteractiveState.DONE

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


# ─────────────────────────────────────────────
# 3.4  SSH Executor (pure paramiko)
# ─────────────────────────────────────────────

# Command allowlist — must match CLAUDE.md
COMMAND_ALLOWLIST_PREFIXES = [
    "ipmcget", "ipmcset", "ipmitool", "curl", "snmpget", "snmpwalk",
]


def is_command_allowed(command: str) -> bool:
    cmd_name = command.strip().split()[0] if command.strip() else ""
    return any(cmd_name.startswith(prefix) for prefix in COMMAND_ALLOWLIST_PREFIXES)


class SSHExecutor:
    """SSH connection pool with exec_command and interactive shell support."""

    def __init__(self):
        import paramiko
        self._paramiko = paramiko
        self._connections: dict[str, "paramiko.SSHClient"] = {}

    def get_connection(self, host: str, port: int = 22,
                       username: str = "root", password: str = "") -> "paramiko.SSHClient":
        key = f"{host}:{port}"
        if key not in self._connections:
            client = self._paramiko.SSHClient()
            client.set_missing_host_key_policy(self._paramiko.AutoAddPolicy())
            client.connect(host, port=port, username=username,
                           password=password, timeout=15)
            self._connections[key] = client
        return self._connections[key]

    def run_command(self, host: str, port: int, command: str,
                    timeout: int = 30) -> tuple[int, str, str]:
        """Non-interactive exec_command. Returns (exit_code, stdout, stderr)."""
        client = self.get_connection(host, port)
        _, stdout, stderr = client.exec_command(command, timeout=timeout)
        exit_code = stdout.channel.recv_exit_status()
        return exit_code, stdout.read().decode(), stderr.read().decode()

    def run_interactive(self, host: str, port: int, initial_command: str,
                        steps: list[dict], timeout: int = 60) -> tuple[bool, str]:
        """Interactive shell via state-machine. Pure paramiko, no pexpect."""
        client = self.get_connection(host, port)
        channel = client.invoke_shell()
        channel.settimeout(timeout)
        session = InteractiveSession(channel, initial_command, steps, timeout)
        try:
            return session.run()
        finally:
            channel.close()

    def close_all(self):
        for client in self._connections.values():
            try:
                client.close()
            except Exception:
                pass
        self._connections.clear()


# ─────────────────────────────────────────────
# 3.5  Action Handler with Secret Redaction
# ─────────────────────────────────────────────

@dataclass
class StepResult:
    id: str
    status: str          # "pass" | "fail" | "error"
    note: str = ""
    stdout: str = ""
    stderr: str = ""


class ActionHandler:
    def __init__(self, ssh: SSHExecutor, max_repairs: int = 3):
        self.ssh = ssh
        self.results: list[StepResult] = []
        self.repair_count = 0
        self.max_repairs = max_repairs

    def handle(self, action: dict) -> StepResult:
        handler_map = {
            "command_plan":              self._handle_command,
            "interactive_command_plan":  self._handle_interactive,
            "health_check_request":      self._handle_health_check,
            "repair_action":             self._handle_repair,
            "completion_summary":        self._handle_summary,
            "error":                     self._handle_error,
        }
        handler = handler_map.get(action["type"])
        if not handler:
            r = StepResult(id=action.get("id", "?"), status="error",
                           note=f"Unknown type: {action['type']}")
            self.results.append(r)
            return r
        result = handler(action)
        self.results.append(result)
        return result

    def _handle_command(self, action: dict) -> StepResult:
        if not is_command_allowed(action["command"]):
            return StepResult(id=action["id"], status="error",
                              note=f"Command blocked by allowlist: {action['command']}")
        target = action["target"]
        try:
            exit_code, stdout, stderr = self.ssh.run_command(
                target["host"], target.get("port", 22),
                action["command"], action.get("timeout_seconds", 30))
        except Exception as e:
            return StepResult(id=action["id"], status="error", note=str(e))

        expected_rc = action.get("expected_exit_code", 0)
        if exit_code != expected_rc:
            return StepResult(id=action["id"], status="fail",
                              note=f"Exit {exit_code} != expected {expected_rc}",
                              stdout=stdout, stderr=stderr)

        for kw in action.get("expected_output_contains", []):
            if kw not in stdout:
                return StepResult(id=action["id"], status="fail",
                                  note=f"Missing in output: '{kw}'", stdout=stdout)

        return StepResult(id=action["id"], status="pass", note="OK", stdout=stdout)

    def _handle_interactive(self, action: dict) -> StepResult:
        if not is_command_allowed(action["initial_command"]):
            return StepResult(id=action["id"], status="error",
                              note=f"Command blocked: {action['initial_command']}")
        target = action["target"]
        try:
            success, output = self.ssh.run_interactive(
                target["host"], target.get("port", 22),
                action["initial_command"], action["steps"],
                action.get("timeout_seconds", 60))
        except Exception as e:
            return StepResult(id=action["id"], status="error", note=str(e))

        if not success:
            return StepResult(id=action["id"], status="fail",
                              note=output, stdout=output)

        for kw in action.get("expected_final_output_contains", []):
            if kw not in output:
                return StepResult(id=action["id"], status="fail",
                                  note=f"Missing in final output: '{kw}'", stdout=output)

        return StepResult(id=action["id"], status="pass",
                          note="Interactive command completed", stdout=output)

    def _handle_health_check(self, action: dict) -> StepResult:
        target = action["target"]
        failed = []
        for check in action["checks"]:
            try:
                exit_code, stdout, _ = self.ssh.run_command(
                    target["host"], target.get("port", 22),
                    check["command"], check.get("timeout_seconds", 10))
            except Exception as e:
                failed.append(f"{check['name']}: {e}")
                continue
            if "expect_exit_code" in check and exit_code != check["expect_exit_code"]:
                failed.append(f"{check['name']}: exit={exit_code}")
            for kw in check.get("expect_output_contains", []):
                if kw not in stdout:
                    failed.append(f"{check['name']}: missing '{kw}'")
        if failed:
            return StepResult(id=action["id"], status="fail", note="; ".join(failed))
        return StepResult(id=action["id"], status="pass", note="All checks passed")

    def _handle_repair(self, action: dict) -> StepResult:
        if self.repair_count >= self.max_repairs:
            return StepResult(id=action["id"], status="error",
                              note=f"Repair limit ({self.max_repairs}) exceeded")
        self.repair_count += 1
        target = action["target"]
        for cmd in action["repair_commands"]:
            try:
                exit_code, stdout, _ = self.ssh.run_command(
                    target["host"], target.get("port", 22),
                    cmd["command"], cmd.get("timeout_seconds", 15))
            except Exception as e:
                return StepResult(id=action["id"], status="error",
                                  note=f"Repair error: {e}")
            expected = cmd.get("expected_exit_code", 0)
            if exit_code != expected:
                return StepResult(id=action["id"], status="fail",
                                  note=f"Repair cmd failed: exit {exit_code}")
        return StepResult(id=action["id"], status="pass",
                          note=f"Repaired: {action['issue']}")

    def _handle_summary(self, action: dict) -> StepResult:
        return StepResult(id="summary", status=action.get("status", "unknown"),
                          note=json.dumps(action, ensure_ascii=False))

    def _handle_error(self, action: dict) -> StepResult:
        return StepResult(id="error", status="error",
                          note=action.get("reason", "unknown agent error"))


# ─────────────────────────────────────────────
# 3.6  Secret Redaction Logger
# ─────────────────────────────────────────────

def _collect_secrets(action: dict) -> list[str]:
    """Extract secret values from an action for log redaction."""
    secrets = []
    if action["type"] == "interactive_command_plan":
        for step in action.get("steps", []):
            if step.get("is_secret"):
                resolved = _resolve_env(step["send_input"])
                if resolved and not resolved.startswith("<MISSING:"):
                    secrets.append(resolved)
    return secrets


def _redact(text: str, secrets: list[str]) -> str:
    """Replace all secret values in text with '***'."""
    for secret in secrets:
        if secret:
            text = text.replace(secret, "***")
    return text


def _log_step(test_id: str, action: dict, result: StepResult):
    """Log step result with secret redaction."""
    secrets = _collect_secrets(action)
    icon = "PASS" if result.status == "pass" else "FAIL"
    logger.info("[%s] %s:%s — %s", icon, action["type"],
                action.get("id", "?"), _redact(result.note, secrets))
    if result.stdout:
        redacted = _redact(result.stdout[:200].replace("\n", "\\n"), secrets)
        logger.debug("  stdout: %s", redacted)


# ─────────────────────────────────────────────
# 3.7  Main Runner with Context Chaining
# ─────────────────────────────────────────────

def build_agent_prompt(test_case: dict, context: str = "") -> str:
    """Build prompt for Claude CLI. CLAUDE.md is loaded automatically."""
    parts = [
        "Execute the following BMC test case.",
        "",
        f"Test Case ID: {test_case['id']}",
        f"Title: {test_case['title']}",
        f"Target Host: {test_case['target_host']}",
        "Steps:",
    ]
    for i, step in enumerate(test_case["steps"], 1):
        parts.append(f"  {i}. {step}")

    if context:
        parts.append("")
        parts.append("Previous Context (from prior test case):")
        parts.append(context)

    return "\n".join(parts)


def run_test_case(test_case: dict, context: str = "") -> tuple[dict, str]:
    """
    Run one test case. Returns (result_dict, next_context_summary).

    Example of context chaining:
        # Test case 1: change password
        result1, ctx1 = run_test_case(tc1, context="")
        # ctx1 = "Password changed from old to new. User enabled."

        # Test case 2: verify new password works — receives ctx1
        result2, ctx2 = run_test_case(tc2, context=ctx1)
        # Agent sees: "Previous Context: Password changed from old to new..."
    """
    ssh = SSHExecutor()
    handler = ActionHandler(ssh)
    accumulator = DeltaAccumulator()

    prompt = build_agent_prompt(test_case, context)

    process = subprocess.Popen(
        ["claude", "-p", prompt, "--output-format", "stream-json"],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE,
        text=True, bufsize=1
    )

    final_summary = None
    aborted = False

    try:
        for raw_line in process.stdout:
            raw_line = raw_line.rstrip("\n")
            if not raw_line:
                continue

            try:
                envelope = json.loads(raw_line)
            except json.JSONDecodeError:
                continue

            # Extract text deltas — the brace-counting accumulator handles
            # arbitrary fragment boundaries correctly
            if (envelope.get("type") == "content_block_delta"
                    and envelope.get("delta", {}).get("type") == "text_delta"):
                accumulator.feed(envelope["delta"].get("text", ""))

            for action in accumulator.extract_actions():
                result = handler.handle(action)
                _log_step(test_case["id"], action, result)

                if action["type"] == "completion_summary":
                    final_summary = action

                if result.status in ("fail", "error") and not aborted:
                    policy = action.get("on_failure",
                                action.get("on_any_failure",
                                action.get("on_repair_failure", "abort")))
                    if policy == "abort":
                        aborted = True
                        process.terminate()

        if not aborted:
            for action in accumulator.flush():
                result = handler.handle(action)
                _log_step(test_case["id"], action, result)
                if action["type"] == "completion_summary":
                    final_summary = action

    except Exception as e:
        logger.error("Test %s crashed: %s", test_case["id"], e)
    finally:
        try:
            process.wait(timeout=10)
        except subprocess.TimeoutExpired:
            process.kill()
        ssh.close_all()

    next_ctx = ""
    if final_summary:
        next_ctx = final_summary.get("next_context_summary", "") or ""

    return {
        "test_case": test_case["id"],
        "result": final_summary.get("status") if final_summary else "error",
        "failed_step_id": final_summary.get("failed_step_id") if final_summary else None,
        "steps": [{"id": r.id, "status": r.status, "note": r.note}
                  for r in handler.results],
        "agent_summary": final_summary
    }, next_ctx


# ─────────────────────────────────────────────
# 3.8  Batch Runner with Context Chaining
# ─────────────────────────────────────────────

def run_all_tests(test_suite_path: str) -> list[dict]:
    """
    Run all test cases sequentially, passing next_context_summary
    from each case to the next.

    Context chain example:
        TC1 (change password) → ctx: "Password changed to NewPass"
        TC2 (verify login)    → receives that context, knows new password
        TC3 (query fan speed)  → receives TC2's context
    """
    with open(test_suite_path) as f:
        suite = json.load(f)

    results = []
    context = ""  # cross-case context chain starts empty

    for tc in suite["test_cases"]:
        logger.info("=" * 60)
        logger.info("Running: %s — %s", tc["id"], tc["title"])
        if context:
            logger.info("Injecting context from previous case: %.200s", context)
        logger.info("=" * 60)

        result, context = run_test_case(tc, context)
        results.append(result)

        logger.info("Result: %s", result["result"].upper())
        if result.get("failed_step_id"):
            logger.info("Failed at: %s", result["failed_step_id"])
        if context:
            logger.info("Context for next case: %.200s", context)

    # Summary
    passed  = sum(1 for r in results if r["result"] == "pass")
    failed  = sum(1 for r in results if r["result"] == "fail")
    errors  = sum(1 for r in results if r["result"] == "error")
    logger.info("=" * 60)
    logger.info("TOTAL: %d | PASS: %d | FAIL: %d | ERROR: %d",
                len(results), passed, failed, errors)

    return results


def _resolve_env(text: str) -> str:
    """Replace $ENV{VAR} placeholders with os.environ values."""
    import os
    return re.sub(
        r'\$ENV\{(\w+)\}',
        lambda m: os.environ.get(m.group(1), f"<MISSING:{m.group(1)}>"),
        text,
    )


if __name__ == "__main__":
    import sys
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s [%(levelname)s] %(message)s")
    suite_path = sys.argv[1] if len(sys.argv) > 1 else "test_suite.json"
    run_all_tests(suite_path)
```

---

## 4. ssh.py Enhancement Suggestions

Pure paramiko implementation — no pexpect dependency, works on both Windows and Linux. Built on `invoke_shell()` with `sendline()`/`expect()` API and automatic secret redaction in logs.

### 4.1 Problem

`exec_command()` runs the command in a non-interactive channel. Commands that prompt for input (password changes, confirmations) either hang or fail silently. The naive workaround of `invoke_shell()` + `time.sleep()` is fragile and timeout-prone.

### 4.2 Suggested Enhancement: `InteractiveCommandRunner`

Add this class to your existing `ssh.py` (or a new `ssh_interactive.py`). This is **pure paramiko** — no pexpect, no external dependencies beyond paramiko itself. Works identically on Windows and Linux.

```python
"""
Pexpect-style interactive command runner over paramiko.
Pure paramiko — no pexpect dependency. Windows/Linux compatible.
"""

import re
import os
import time
import logging
from typing import Optional

logger = logging.getLogger(__name__)


class PromptTimeout(Exception):
    """Raised when an expected prompt is not seen within the timeout."""
    pass


# ─────────────────────────────────────────────
# Secret Redaction Helper
# ─────────────────────────────────────────────

class SecretRedactor:
    """
    Tracks secret values and redacts them from log output.
    Register secrets via add(), then use redact() on any text before logging.
    """

    def __init__(self):
        self._secrets: set[str] = set()

    def add(self, secret: str) -> None:
        """Register a secret value for redaction."""
        if secret and not secret.startswith("<MISSING:"):
            self._secrets.add(secret)

    def redact(self, text: str) -> str:
        """Replace all registered secrets with '***'."""
        for s in self._secrets:
            text = text.replace(s, "***")
        return text


# ─────────────────────────────────────────────
# InteractiveCommandRunner (pure paramiko)
# ─────────────────────────────────────────────

class InteractiveCommandRunner:
    """
    Pexpect-like interface built on paramiko's invoke_shell().
    No pexpect dependency — uses only paramiko + stdlib.
    Works on Windows and Linux identically.

    Usage:
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

    def __init__(self, ssh_client, width=200, height=50, banner_timeout=2.0):
        self.channel = ssh_client.invoke_shell(width=width, height=height)
        self.channel.settimeout(0.1)  # non-blocking reads
        self.buffer: str = ""
        self.full_output: str = ""
        self._expect_scan_pos: int = 0
        self.redactor = SecretRedactor()

        # Drain the login banner so it doesn't pollute prompt matching
        self._drain(banner_timeout)
        self._expect_scan_pos = len(self.buffer)  # skip banner text

    # -- Core API -----------------------------------------------------------

    def sendline(self, text: str, redact: bool = False) -> None:
        """Send a line of text (appends \\n automatically).
        If redact=True, the value is registered for log redaction."""
        if redact:
            resolved = self._resolve_env(text)
            self.redactor.add(resolved)
            logger.debug("SEND: ***")
        else:
            logger.debug("SEND: %s", text)
        actual_text = self._resolve_env(text)
        self.channel.send((actual_text + "\n").encode("utf-8"))

    def expect(self, pattern: str, timeout: float = 10.0) -> str:
        """
        Block until pattern appears in output (case-insensitive).

        Parameters:
            pattern:  Literal substring or regex.
            timeout:  Seconds to wait before raising PromptTimeout.

        Returns:
            The full buffer at the point of match.

        Raises:
            PromptTimeout: If pattern not found within timeout.
        """
        deadline = time.monotonic() + timeout
        scan_start = self._expect_scan_pos

        while time.monotonic() < deadline:
            chunk = self._read_chunk()
            if chunk:
                self.buffer += chunk
                self.full_output += chunk

            new_region = self.buffer[scan_start:]

            # Case-insensitive substring match (fast path)
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
                pass  # not valid regex — substring was the only check

            time.sleep(0.05)

        # Timeout — redact buffer tail before including in error message
        safe_tail = self.redactor.redact(self.buffer[-300:])
        raise PromptTimeout(
            f"Timeout after {timeout:.1f}s waiting for {pattern!r}.  "
            f"Buffer tail: …{safe_tail}"
        )

    def collect_remaining(self, timeout: float = 3.0) -> str:
        """Drain output for timeout seconds, then return full_output."""
        self._drain(timeout)
        return self.full_output

    def close(self) -> None:
        """Close the underlying shell channel."""
        try:
            self.channel.close()
        except Exception:
            pass

    # -- Convenience: run a full interactive plan ---------------------------

    def run_steps(self, initial_command: str, steps: list[dict],
                  final_timeout: float = 3.0) -> tuple[bool, str]:
        """
        Execute initial_command, then walk through steps (expect/send pairs).

        Each step dict must have:
            expect_prompt:  str — substring or regex to wait for
            send_input:     str — text to send (may use $ENV{VAR})
            timeout_sec:    int — per-step timeout (REQUIRED)
            is_secret:      bool — optional, redact from logs
        """
        try:
            self.sendline(initial_command)
            for step in steps:
                self.expect(
                    step["expect_prompt"],
                    timeout=step["timeout_sec"],  # required, no default
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
        """Replace $ENV{VAR} placeholders with os.environ values."""
        return re.sub(
            r'\$ENV\{(\w+)\}',
            lambda m: os.environ.get(m.group(1), f"<MISSING:{m.group(1)}>"),
            text,
        )


# ─────────────────────────────────────────────
# MockChannel — for unit testing without hardware
# ─────────────────────────────────────────────

class MockChannel:
    """
    Simulates a paramiko shell channel that plays back scripted output.
    For unit testing interactive flows without SSH connectivity.

    Usage:
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
        assert ok
        assert "successfully" in output
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

    def close(self): self._closed = True

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


# ─────────────────────────────────────────────
# Self-Test (run with: python ssh_interactive.py)
# ─────────────────────────────────────────────

def _self_test():
    """Smoke test — password change flow with MockChannel + secret redaction."""
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

    # Verify secret redaction works
    redacted = runner.redactor.redact("Password is OldPass and NewPass")
    assert "OldPass" not in redacted, f"Secret not redacted: {redacted}"
    assert "NewPass" not in redacted, f"Secret not redacted: {redacted}"
    assert "***" in redacted

    print("SELF-TEST PASSED")
    print(f"  Output: {output!r}")
    print(f"  Redaction test: {redacted!r}")


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format="%(levelname)s %(message)s")
    _self_test()
```

### 4.3 Integration with Action Handler

Replace the `run_interactive` method in your SSH executor:

```python
def run_interactive(self, host, port, initial_command, steps, timeout=60):
    client = self.get_connection(host, port)
    runner = InteractiveCommandRunner(client)
    try:
        return runner.run_steps(initial_command, steps, final_timeout=3)
    except PromptTimeout as e:
        return False, str(e)
    finally:
        runner.close()
```

### 4.4 Key Differences from exec_command

| Aspect | `exec_command()` | `InteractiveCommandRunner` |
|--------|------------------|----------------------------|
| PTY allocation | No | Yes (via `invoke_shell`) |
| Prompt detection | N/A | Case-insensitive substring + regex |
| Timeout handling | Global only | Per-step `timeout_sec` (required) + global |
| Secret redaction | N/A | `SecretRedactor` replaces secrets with `***` in all logs and error messages |
| Output buffering | Read all at end | Continuous accumulation with scan-position tracking |
| Error diagnostics | Generic timeout | Buffer tail (redacted) included in error |
| Login banner | N/A | Auto-drained on init |
| Dependencies | paramiko only | paramiko only (no pexpect) |
| Platform | Windows + Linux | Windows + Linux |

---

## Appendix A: Quick-Start Checklist

1. Copy Section 1 into `CLAUDE.md` at your project root
2. Load JSON schemas (Section 2) into your runner for validation
3. Implement the runner (Section 3) — start with `DeltaAccumulator` + `ActionHandler`
4. Enhance `ssh.py` with `InteractiveCommandRunner` (Section 4)
5. Create a `test_suite.json` with one simple test case (e.g., `ipmcget -d deviceinfo`)
6. Run: `python bmc_test_runner.py test_suite.json`

## Appendix B: Environment Variables

| Variable | Purpose | Example |
|----------|---------|---------|
| `OLD_PASSWORD` | Current password for credential change tests | `Admin@123` |
| `NEW_PASSWORD` | New password to set | `NewAdmin@456` |
| `BMC_HOST` | Default target BMC IP | `192.168.1.100` |
| `BMC_USER` | SSH username | `root` |
| `BMC_PASS` | SSH password | *(set in env, never in files)* |
| `BMC_TOKEN` | Redfish session token for curl | *(set in env)* |

## Appendix C: Cross-Case Context Chaining Example

```
Test Suite: [TC1_change_password, TC2_verify_login, TC3_query_fans]

TC1 runs → agent emits:
  {"type":"completion_summary",...,"next_context_summary":"Password changed from Admin@123 to NewAdmin@456. User testuser enabled."}

TC2 runs with prompt including:
  "Previous Context (from prior test case):
   Password changed from Admin@123 to NewAdmin@456. User testuser enabled."
→ agent knows the new password and can verify login with it.

TC2 completes → agent emits:
  {"type":"completion_summary",...,"next_context_summary":"Login verified with new password. BMC firmware V5.05.00.12. 6 fans online."}

TC3 runs with that context → agent can reference firmware version and fan count.
```
