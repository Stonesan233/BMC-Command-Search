# Unattended BMC Agent Testing — External Implementation Package

> **Version**: 1.0 | **Date**: 2026-03-23
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

## Decision Rules

1. **Before any credential or destructive operation** → emit `health_check_request` first.
2. **If a command has ANY interactive prompt** (password, yes/no, menu) → use `interactive_command_plan`, never `command_plan`.
3. **If a health check fails** → emit `repair_action`, then retry the check. Max 3 repair cycles.
4. **Always include a `postcondition` phase** to confirm the system is in expected state after changes.
5. **Phase ordering**: `precondition` → `execute` → `postcondition`. Never skip.

## MCP Tool Usage

You have access to the `bmc_commands_search` MCP server. Use it to look up exact
command syntax before emitting any `command_plan` or `interactive_command_plan`.
Search by keyword (e.g., "user password", "fan speed", "firmware version").
Use the returned command details (syntax, parameters, expected output format) to
build accurate plans.

## Inline Examples

### Example 1: Simple non-interactive query

```
{"type":"command_plan","id":"cmd_001","phase":"precondition","description":"Verify BMC is reachable","target":{"host":"{{TARGET_HOST}}","port":22,"protocol":"ssh"},"command":"ipmcget -d deviceinfo","timeout_seconds":15,"expected_exit_code":0,"expected_output_contains":["Board ID"],"on_failure":"abort"}
```

### Example 2: Interactive password change

```
{"type":"interactive_command_plan","id":"icmd_001","phase":"execute","description":"Change testuser password","target":{"host":"{{TARGET_HOST}}","port":22,"protocol":"ssh"},"initial_command":"ipmcset -t user -d password -v testuser","timeout_seconds":60,"steps":[{"step":1,"expect_prompt":"current password","send_input":"$ENV{OLD_PASSWORD}","is_secret":true,"timeout_seconds":10},{"step":2,"expect_prompt":"new password","send_input":"$ENV{NEW_PASSWORD}","is_secret":true,"timeout_seconds":10},{"step":3,"expect_prompt":"confirm","send_input":"$ENV{NEW_PASSWORD}","is_secret":true,"timeout_seconds":10}],"expected_final_output_contains":["success"],"on_failure":"repair"}
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
{"type":"completion_summary","test_case":"TC_USER_PASSWORD_CHANGE_001","result":"pass","steps_executed":5,"steps_passed":5,"steps_failed":0,"repairs_attempted":0,"repairs_succeeded":0,"duration_hint_seconds":35,"details":[{"id":"hc_001","status":"pass","note":"Preconditions met"},{"id":"cmd_001","status":"pass","note":"User verified"},{"id":"icmd_001","status":"pass","note":"Password changed"},{"id":"hc_002","status":"pass","note":"Postconditions met"}],"error_message":null,"next_context_summary":"Password for testuser changed from OldPass to NewPass. User is enabled. BMC firmware V5.05.00.12."}
```

## Critical Constraints

- **Command allowlist**: Only emit commands starting with `ipmcget`, `ipmcset`, `ipmctool`, `ipmcflash`, `cat`, `grep`, `ls`. Anything else will be rejected by the runner.
- **No shell metacharacters**: Never use `$()`, backticks, pipes, or redirects in command fields. The runner calls `exec_command()` directly (no shell expansion).
- **Secrets**: Use `$ENV{VAR_NAME}` placeholders for passwords/tokens. The runner resolves these at runtime. Mark steps containing secrets with `"is_secret": true`.
- **One JSON per line**: Partial JSON or multi-line JSON will be silently dropped.
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
        "required": ["step", "expect_prompt", "send_input"],
        "additionalProperties": false,
        "properties": {
          "step":            { "type": "integer", "minimum": 1 },
          "expect_prompt":   { "type": "string", "minLength": 1 },
          "send_input":      { "type": "string" },
          "is_secret":       { "type": "boolean", "default": false },
          "timeout_seconds": { "type": "integer", "minimum": 1, "default": 10 }
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

### 2.5 `completion_summary` (with `next_context_summary`)

The `next_context_summary` field enables **cross-case context passing**. When the runner starts the next test case, it injects this string into the agent prompt as `Previous Context`. This allows the agent to know what changed in prior cases (e.g., "password was changed from X to Y", "firmware was upgraded to V5.06").

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "completion_summary",
  "type": "object",
  "required": ["type", "test_case", "result", "steps_executed", "steps_passed", "steps_failed",
               "repairs_attempted", "repairs_succeeded", "details"],
  "additionalProperties": false,
  "properties": {
    "type":                  { "const": "completion_summary" },
    "test_case":             { "type": "string" },
    "result":                { "type": "string", "enum": ["pass", "fail", "error"] },
    "steps_executed":        { "type": "integer", "minimum": 0 },
    "steps_passed":          { "type": "integer", "minimum": 0 },
    "steps_failed":          { "type": "integer", "minimum": 0 },
    "repairs_attempted":     { "type": "integer", "minimum": 0 },
    "repairs_succeeded":     { "type": "integer", "minimum": 0 },
    "duration_hint_seconds": { "type": "integer", "minimum": 0 },
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
    "error_message":         { "type": ["string", "null"], "default": null },
    "next_context_summary":  {
      "type": ["string", "null"],
      "default": null,
      "description": "Free-text summary of state changes for the next test case. The runner injects this into the next agent invocation's prompt as 'Previous Context'. Include: what changed, current credential state, firmware versions, any anomalies observed."
    }
  }
}
```

**Usage pattern in the runner:**

```python
# After test case N completes:
context_for_next = summary.get("next_context_summary", "")

# When building prompt for test case N+1:
prompt = build_agent_prompt(next_test_case, context=context_for_next)
```

---

## 3. Test Runner Pseudo-Code

Key improvements over the original spec:
- **Proper stream-json delta accumulation**: text deltas arrive as arbitrary UTF-8 fragments (may split mid-character, mid-JSON-key). The runner accumulates into a buffer and only attempts JSON extraction on complete lines.
- **State machine for interactive command execution**: explicit states (`WAITING_PROMPT`, `SENDING_INPUT`, `COLLECTING_OUTPUT`) instead of sleep-based polling.
- **Schema validation** before execution.
- **Cross-case context passing** via `next_context_summary`.

```python
#!/usr/bin/env python3
"""
BMC Agent-Driven Test Runner — External Implementation
Launches Claude CLI with stream-json, accumulates text deltas,
extracts structured JSON actions, executes them via SSH.
"""

import subprocess
import json
import re
import time
import enum
import logging
from dataclasses import dataclass, field
from typing import Optional

# Optional: pip install jsonschema
try:
    import jsonschema
    HAS_JSONSCHEMA = True
except ImportError:
    HAS_JSONSCHEMA = False

logger = logging.getLogger("bmc_runner")


# ─────────────────────────────────────────────
# 3.1  Stream-JSON Delta Accumulator
# ─────────────────────────────────────────────

STRUCTURED_TYPES = {
    "command_plan", "interactive_command_plan",
    "health_check_request", "repair_action", "completion_summary"
}

# Load schemas from files or inline dicts (omitted for brevity — use Section 2)
SCHEMAS: dict[str, dict] = {}  # type_name -> JSON Schema dict


class DeltaAccumulator:
    """
    Accumulates text_delta fragments from Claude's stream-json output.

    Claude's stream-json format emits events like:
        {"type":"content_block_delta","index":0,"delta":{"type":"text_delta","text":"..."}}

    The "text" field may split at ANY byte boundary — mid-word, mid-JSON-key,
    even mid-UTF-8 codepoint. This class handles that correctly.
    """

    def __init__(self):
        self._buffer = ""            # raw accumulated text
        self._extracted_pos = 0      # position up to which we've extracted complete lines

    def feed(self, text_fragment: str):
        """Append a text_delta fragment to the buffer."""
        self._buffer += text_fragment

    def extract_actions(self) -> list[dict]:
        """
        Scan the buffer for complete JSON lines. A "complete line" is text
        ending with \\n whose content parses as JSON with a valid type field.

        Returns extracted actions and advances the scan position.
        Does NOT consume incomplete (non-newline-terminated) trailing text,
        because the next delta may complete it.
        """
        actions = []
        # Only scan text that ends with a newline (i.e., complete lines)
        last_newline = self._buffer.rfind("\n", self._extracted_pos)
        if last_newline < self._extracted_pos:
            return actions  # no new complete lines yet

        scannable = self._buffer[self._extracted_pos:last_newline + 1]
        self._extracted_pos = last_newline + 1

        for line in scannable.splitlines():
            line = line.strip()
            if not line or not line.startswith("{"):
                continue
            try:
                obj = json.loads(line)
            except json.JSONDecodeError:
                continue

            if not isinstance(obj, dict):
                continue
            if obj.get("type") not in STRUCTURED_TYPES:
                continue

            # Optional schema validation
            if HAS_JSONSCHEMA and obj["type"] in SCHEMAS:
                try:
                    jsonschema.validate(obj, SCHEMAS[obj["type"]])
                except jsonschema.ValidationError as e:
                    logger.warning("Schema validation failed for %s: %s",
                                   obj.get("id", "?"), e.message)
                    continue

            actions.append(obj)

        return actions

    def flush(self) -> list[dict]:
        """Final extraction — treat any remaining text as complete."""
        self._buffer += "\n"  # force-terminate last line
        return self.extract_actions()


# ─────────────────────────────────────────────
# 3.2  Interactive Command State Machine
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
    State-machine-based interactive command executor.
    Replaces naive sleep-poll loops with explicit state transitions.
    """

    def __init__(self, channel, initial_command: str, steps: list[dict],
                 total_timeout: int = 60):
        self.channel = channel
        self.initial_command = initial_command
        self.steps = steps
        self.total_timeout = total_timeout
        self.state = InteractiveState.SEND_INITIAL
        self.current_step_idx = 0
        self.output_buffer = ""
        self.step_buffer = ""
        self.deadline = time.monotonic() + total_timeout
        self.error_message = ""

    def run(self) -> tuple[bool, str]:
        """Execute the state machine. Returns (success, full_output)."""
        while self.state not in (InteractiveState.DONE,
                                  InteractiveState.TIMEOUT,
                                  InteractiveState.ERROR):
            if time.monotonic() > self.deadline:
                self.state = InteractiveState.TIMEOUT
                self.error_message = (
                    f"Global timeout ({self.total_timeout}s) exceeded "
                    f"at step {self.current_step_idx + 1}"
                )
                break
            self._tick()

        success = self.state == InteractiveState.DONE
        if not success and not self.error_message:
            self.error_message = f"Ended in state {self.state.value}"
        return success, self.output_buffer if success else self.error_message

    def _tick(self):
        if self.state == InteractiveState.SEND_INITIAL:
            self.channel.send(self.initial_command + "\n")
            self.state = InteractiveState.WAITING_PROMPT
            self.step_buffer = ""

        elif self.state == InteractiveState.WAITING_PROMPT:
            chunk = self._recv_nonblocking()
            if chunk:
                self.step_buffer += chunk
                self.output_buffer += chunk

            if self.current_step_idx >= len(self.steps):
                # All steps done — collect remaining output
                self.state = InteractiveState.COLLECTING_TAIL
                return

            step = self.steps[self.current_step_idx]
            prompt_pattern = step["expect_prompt"]

            # Check step-level timeout
            step_timeout = step.get("timeout_seconds", 10)
            step_deadline = self.deadline  # bounded by global
            # (A real implementation would track per-step start time)

            if self._matches_prompt(self.step_buffer, prompt_pattern):
                self.state = InteractiveState.SENDING_INPUT

        elif self.state == InteractiveState.SENDING_INPUT:
            step = self.steps[self.current_step_idx]
            input_text = step["send_input"]
            # Resolve $ENV{...} placeholders
            input_text = self._resolve_env_vars(input_text)
            self.channel.send(input_text + "\n")
            self.current_step_idx += 1
            self.step_buffer = ""
            self.state = InteractiveState.WAITING_PROMPT

        elif self.state == InteractiveState.COLLECTING_TAIL:
            # Drain remaining output for 2 seconds
            tail_deadline = min(time.monotonic() + 2.0, self.deadline)
            while time.monotonic() < tail_deadline:
                chunk = self._recv_nonblocking()
                if chunk:
                    self.output_buffer += chunk
                else:
                    time.sleep(0.1)
            self.state = InteractiveState.DONE

    def _recv_nonblocking(self) -> str:
        if self.channel.recv_ready():
            return self.channel.recv(4096).decode("utf-8", errors="replace")
        time.sleep(0.1)
        return ""

    def _matches_prompt(self, buffer: str, pattern: str) -> bool:
        """Match prompt as substring or regex."""
        if pattern in buffer:
            return True
        try:
            return bool(re.search(pattern, buffer))
        except re.error:
            return False

    @staticmethod
    def _resolve_env_vars(text: str) -> str:
        """Replace $ENV{VAR_NAME} with os.environ value."""
        import os
        def replacer(m):
            return os.environ.get(m.group(1), f"<MISSING:{m.group(1)}>")
        return re.sub(r'\$ENV\{(\w+)\}', replacer, text)


# ─────────────────────────────────────────────
# 3.3  SSH Executor (enhanced)
# ─────────────────────────────────────────────

class SSHExecutor:
    """SSH connection pool with both exec_command and interactive support."""

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
        """Non-interactive command via exec_command. Returns (exit_code, stdout, stderr)."""
        client = self.get_connection(host, port)
        _, stdout, stderr = client.exec_command(command, timeout=timeout)
        exit_code = stdout.channel.recv_exit_status()
        return exit_code, stdout.read().decode(), stderr.read().decode()

    def run_interactive(self, host: str, port: int, initial_command: str,
                        steps: list[dict], timeout: int = 60) -> tuple[bool, str]:
        """Interactive command via state-machine-driven shell session."""
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
# 3.4  Action Handler
# ─────────────────────────────────────────────

@dataclass
class StepResult:
    id: str
    status: str          # "pass" | "fail" | "error"
    note: str = ""
    stdout: str = ""
    stderr: str = ""


# Command allowlist — reject anything not matching
COMMAND_ALLOWLIST_PREFIXES = [
    "ipmcget", "ipmcset", "ipmctool", "ipmcflash",
    "cat", "grep", "ls", "echo",
]


def is_command_allowed(command: str) -> bool:
    cmd_name = command.strip().split()[0] if command.strip() else ""
    return any(cmd_name.startswith(prefix) for prefix in COMMAND_ALLOWLIST_PREFIXES)


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

        return StepResult(id=action["id"], status="pass",
                          note="OK", stdout=stdout)

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
                                  note=f"Missing in final output: '{kw}'",
                                  stdout=output)

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
            return StepResult(id=action["id"], status="fail",
                              note="; ".join(failed))
        return StepResult(id=action["id"], status="pass",
                          note="All checks passed")

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
        return StepResult(id="summary", status=action.get("result", "unknown"),
                          note=json.dumps(action, ensure_ascii=False))


# ─────────────────────────────────────────────
# 3.5  Main Runner with Delta Accumulation
# ─────────────────────────────────────────────

def build_agent_prompt(test_case: dict, context: str = "") -> str:
    """Build prompt for Claude CLI. The CLAUDE.md system prompt is loaded automatically."""
    parts = [
        f"Execute the following BMC test case.",
        f"",
        f"Test Case ID: {test_case['id']}",
        f"Title: {test_case['title']}",
        f"Target Host: {test_case['target_host']}",
        f"Steps:",
    ]
    for i, step in enumerate(test_case["steps"], 1):
        parts.append(f"  {i}. {step}")

    if context:
        parts.append(f"")
        parts.append(f"Previous Context (from prior test case):")
        parts.append(context)

    return "\n".join(parts)


def run_test_case(test_case: dict, context: str = "") -> tuple[dict, str]:
    """
    Run one test case. Returns (result_dict, next_context_summary).
    The next_context_summary is passed to the subsequent test case.
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

            # Parse the stream-json envelope
            try:
                envelope = json.loads(raw_line)
            except json.JSONDecodeError:
                continue

            # Extract text deltas — this is where proper accumulation matters.
            # Claude emits {"type":"content_block_delta","delta":{"type":"text_delta","text":"..."}}
            # The "text" value is an ARBITRARY fragment. It may be a single character,
            # half a JSON key, or multiple complete lines. We must not assume line boundaries.
            if (envelope.get("type") == "content_block_delta"
                    and envelope.get("delta", {}).get("type") == "text_delta"):
                accumulator.feed(envelope["delta"].get("text", ""))

            # After each delta, try to extract complete action lines
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

        # Final flush — catch any trailing text not terminated by newline
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
        "result": final_summary.get("result") if final_summary else "error",
        "steps": [{"id": r.id, "status": r.status, "note": r.note}
                  for r in handler.results],
        "agent_summary": final_summary
    }, next_ctx


def _log_step(test_id: str, action: dict, result: StepResult):
    icon = "PASS" if result.status == "pass" else "FAIL"
    secret = (action["type"] == "interactive_command_plan"
              and any(s.get("is_secret") for s in action.get("steps", [])))
    logger.info("[%s] %s:%s — %s", icon, action["type"], action.get("id", "?"), result.note)
    if result.stdout and not secret:
        logger.debug("  stdout: %.200s", result.stdout.replace("\n", "\\n"))


# ─────────────────────────────────────────────
# 3.6  Batch Runner with Context Chaining
# ─────────────────────────────────────────────

def run_all_tests(test_suite_path: str) -> list[dict]:
    with open(test_suite_path) as f:
        suite = json.load(f)

    results = []
    context = ""  # cross-case context chain

    for tc in suite["test_cases"]:
        logger.info("=" * 60)
        logger.info("Running: %s — %s", tc["id"], tc["title"])
        logger.info("=" * 60)

        result, context = run_test_case(tc, context)
        results.append(result)

        logger.info("Result: %s", result["result"].upper())
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


if __name__ == "__main__":
    import sys
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s [%(levelname)s] %(message)s")
    suite_path = sys.argv[1] if len(sys.argv) > 1 else "test_suite.json"
    run_all_tests(suite_path)
```

---

## 4. ssh.py Enhancement Suggestions

Your existing `ssh.py` uses `paramiko.exec_command()` which is fire-and-forget (no PTY, no interactive prompt handling). Below are pexpect-style enhancements you can apply to support `interactive_command_plan` actions.

### 4.1 Problem

`exec_command()` runs the command in a non-interactive channel. Commands that prompt for input (password changes, confirmations) either hang or fail silently. The naive workaround of `invoke_shell()` + `time.sleep()` is fragile and timeout-prone.

### 4.2 Suggested Enhancement: `InteractiveCommandRunner`

Add this class to your existing `ssh.py` (or a new `ssh_interactive.py`):

```python
"""
Pexpect-style interactive command runner over paramiko.
Drop-in addition to your existing ssh.py module.
"""

import re
import time
import logging
from typing import Optional

logger = logging.getLogger(__name__)


class PromptTimeout(Exception):
    """Raised when an expected prompt is not seen within the timeout."""
    pass


class InteractiveCommandRunner:
    """
    Pexpect-like interface built on paramiko's invoke_shell().

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

    def __init__(self, ssh_client, width=200, height=50):
        self.channel = ssh_client.invoke_shell(width=width, height=height)
        self.channel.settimeout(0.1)  # non-blocking reads
        self.buffer = ""
        self.full_output = ""
        # Drain the login banner
        self._drain(timeout=2.0)

    def sendline(self, text: str, redact: bool = False):
        """Send a line of text followed by newline."""
        display = "***" if redact else text
        logger.debug("SEND: %s", display)
        self.channel.send(text + "\n")

    def expect(self, pattern: str, timeout: float = 10.0) -> str:
        """
        Wait until `pattern` appears in the output buffer.

        Args:
            pattern: Substring or regex to match against accumulated output.
            timeout: Max seconds to wait.

        Returns:
            The buffer contents up to and including the match.

        Raises:
            PromptTimeout: If pattern not found within timeout.
        """
        deadline = time.monotonic() + timeout
        match_start_pos = len(self.buffer)  # only scan new content

        while time.monotonic() < deadline:
            chunk = self._read_chunk()
            if chunk:
                self.buffer += chunk
                self.full_output += chunk

            # Check for match in newly received content
            search_region = self.buffer[match_start_pos:]
            if pattern in search_region:
                logger.debug("MATCHED (substring): %s", pattern)
                return self.buffer
            try:
                if re.search(pattern, search_region):
                    logger.debug("MATCHED (regex): %s", pattern)
                    return self.buffer
            except re.error:
                pass  # pattern is not valid regex, substring check was enough

            time.sleep(0.05)

        # Timeout — include what we received for debugging
        raise PromptTimeout(
            f"Timed out after {timeout}s waiting for '{pattern}'. "
            f"Buffer tail: ...{self.buffer[-200:]}"
        )

    def collect_remaining(self, timeout: float = 3.0) -> str:
        """Drain any remaining output for `timeout` seconds."""
        self._drain(timeout)
        return self.full_output

    def close(self):
        """Close the shell channel."""
        try:
            self.channel.close()
        except Exception:
            pass

    def _read_chunk(self) -> str:
        try:
            if self.channel.recv_ready():
                return self.channel.recv(4096).decode("utf-8", errors="replace")
        except Exception:
            pass
        return ""

    def _drain(self, timeout: float):
        """Read and discard output for `timeout` seconds."""
        deadline = time.monotonic() + timeout
        while time.monotonic() < deadline:
            chunk = self._read_chunk()
            if chunk:
                self.buffer += chunk
                self.full_output += chunk
            else:
                time.sleep(0.1)
```

### 4.3 Integration with Action Handler

Replace the `run_interactive` method in your SSH executor with:

```python
def run_interactive(self, host, port, initial_command, steps, timeout=60):
    client = self.get_connection(host, port)
    runner = InteractiveCommandRunner(client)
    try:
        runner.sendline(initial_command)
        for step in steps:
            runner.expect(step["expect_prompt"],
                          timeout=step.get("timeout_seconds", 10))
            runner.sendline(step["send_input"],
                            redact=step.get("is_secret", False))
        output = runner.collect_remaining(timeout=3)
        return True, output
    except PromptTimeout as e:
        return False, str(e)
    finally:
        runner.close()
```

### 4.4 Key Differences from Your Current ssh.py

| Aspect | Current (`exec_command`) | Enhanced (`InteractiveCommandRunner`) |
|--------|--------------------------|---------------------------------------|
| PTY allocation | No | Yes (via `invoke_shell`) |
| Prompt detection | N/A | Substring + regex matching |
| Timeout handling | Global only | Per-step + global |
| Secret redaction | N/A | `redact=True` on `sendline` |
| Output buffering | Read all at end | Continuous accumulation |
| Error diagnostics | Generic timeout | Buffer tail included in error |
| Login banner | N/A | Auto-drained on init |

### 4.5 Testing the Enhancement Without Real Hardware

```python
# Unit test with a mock channel
class MockChannel:
    """Simulates a paramiko channel for testing."""
    def __init__(self, script: list[tuple[float, str]]):
        # script = [(delay_seconds, text_to_emit), ...]
        self._script = script
        self._start = time.monotonic()
        self._sent = []

    def invoke_shell(self, **kw): return self
    def settimeout(self, t): pass
    def recv_ready(self):
        return bool(self._pending_output())
    def recv(self, n):
        text = self._pending_output()
        return text.encode() if text else b""
    def send(self, data):
        self._sent.append(data)
    def close(self): pass

    def _pending_output(self):
        elapsed = time.monotonic() - self._start
        for delay, text in self._script:
            if elapsed >= delay:
                self._script.remove((delay, text))
                return text
        return None

# Example test
script = [
    (0.5, "Enter current password: "),
    (1.5, "Enter new password: "),
    (2.5, "Confirm new password: "),
    (3.5, "Password changed successfully.\n"),
]
mock = MockChannel(script)
runner = InteractiveCommandRunner.__new__(InteractiveCommandRunner)
runner.channel = mock
runner.buffer = ""
runner.full_output = ""

runner.sendline("ipmcset -t user -d password -v testuser")
runner.expect("current password", timeout=5)
runner.sendline("OldPass", redact=True)
runner.expect("new password", timeout=5)
runner.sendline("NewPass", redact=True)
runner.expect("confirm", timeout=5)
runner.sendline("NewPass", redact=True)
output = runner.collect_remaining(timeout=2)
assert "successfully" in output
```

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
| `BMC_PASS` | SSH password | `***` |
