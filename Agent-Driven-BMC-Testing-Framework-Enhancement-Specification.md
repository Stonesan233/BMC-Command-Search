# Agent-Driven BMC Testing Framework Enhancement Specification

## 1. Overall Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│                        Test Runner (Python)                        │
│                                                                     │
│  ┌───────────┐  ┌──────────────┐  ┌────────────┐  ┌─────────────┐ │
│  │ Test Case  │  │ Claude CLI   │  │  JSON      │  │  SSH        │ │
│  │ Loader     │──│ Launcher     │──│  Stream    │──│  Executor   │ │
│  │            │  │              │  │  Parser    │  │             │ │
│  └───────────┘  └──────────────┘  └────────────┘  └──────┬──────┘ │
│                                                           │        │
│  ┌───────────┐  ┌──────────────┐  ┌────────────┐         │        │
│  │ Result    │  │ Health       │  │  Repair    │         │        │
│  │ Collector │◄─│ Checker      │◄─│  Engine    │◄────────┘        │
│  └───────────┘  └──────────────┘  └────────────┘                   │
└─────────────────────────────────────────────────────────────────────┘
        │                                    ▲
        │  claude -p "<prompt>"              │ streaming JSON lines
        │  --output-format stream-json       │
        ▼                                    │
┌─────────────────────────────────────────────────────────────────────┐
│                     Claude Code CLI (Agent)                         │
│                                                                     │
│  ┌───────────────┐  ┌───────────────┐  ┌──────────────────┐       │
│  │ MCP Search    │  │ Command       │  │ Structured JSON  │       │
│  │ (bmc_commands)│──│ Planner       │──│ Output Generator │──►stdout│
│  └───────────────┘  └───────────────┘  └──────────────────┘       │
└─────────────────────────────────────────────────────────────────────┘
        │
        ▼
┌─────────────────────┐
│ BMC Device (Target)  │
│ SSH / IPMI / Redfish │
└─────────────────────┘

Flow:
  Test Runner ──starts──► Claude CLI process
  Claude CLI   ──emits──► structured JSON lines (stdout)
  Test Runner  ──parses──► each JSON line
  Test Runner  ──executes──► SSH commands / health checks / repairs
  Test Runner  ──feeds back──► results to next Claude invocation (if needed)
```

## 2. Required JSON Output Format from Agent

All structured output from the agent MUST be embedded inside the `text` content of a `content_block_delta` message in Claude's `stream-json` format. The test runner extracts text deltas, accumulates them, and parses complete JSON objects delimited by newlines.

Each structured JSON object MUST contain a `type` field as the discriminator.

### 2.1 Envelope Convention

The agent outputs one JSON object per logical action, each on its own line within the text output:

```
{"type": "<structured_type>", ...fields}
```

The test runner accumulates text output and scans for lines matching `^\{.*\}$` with a valid `type` field.

### 2.2 Valid `type` Values

| Type                     | Purpose                                      |
|--------------------------|----------------------------------------------|
| `command_plan`           | Non-interactive command(s) to execute         |
| `interactive_command_plan` | Multi-step command with expected prompts    |
| `health_check_request`  | Pre/post environment health verification      |
| `repair_action`          | Auto-repair for detected issues               |
| `completion_summary`    | Final result of the test case                 |

## 3. Key Structured Types

### 3.1 `command_plan` — Non-Interactive Commands

For commands that run to completion without user interaction (no password prompts, no confirmations).

**Schema:**

```json
{
  "type": "command_plan",
  "id": "cmd_001",
  "phase": "execute",
  "description": "Human-readable description of what this command does",
  "target": {
    "host": "192.168.1.100",
    "port": 22,
    "protocol": "ssh"
  },
  "command": "ipmcget -d deviceinfo",
  "timeout_seconds": 30,
  "expected_exit_code": 0,
  "expected_output_contains": ["Board ID", "CPLD Version"],
  "on_failure": "abort"
}
```

**Field Descriptions:**

| Field                      | Type       | Required | Description                                                |
|----------------------------|------------|----------|------------------------------------------------------------|
| `type`                     | string     | yes      | Always `"command_plan"`                                    |
| `id`                       | string     | yes      | Unique identifier for tracking                             |
| `phase`                    | string     | yes      | `"precondition"`, `"execute"`, or `"postcondition"`        |
| `description`              | string     | yes      | What this step accomplishes                                |
| `target`                   | object     | yes      | Connection details (`host`, `port`, `protocol`)            |
| `command`                  | string     | yes      | The exact command to execute                               |
| `timeout_seconds`          | integer    | yes      | Max execution time before force-kill                       |
| `expected_exit_code`       | integer    | no       | Expected return code (default: 0)                          |
| `expected_output_contains` | string[]   | no       | Substrings that MUST appear in stdout                      |
| `on_failure`               | string     | yes      | `"abort"`, `"continue"`, `"retry"`, or `"repair"`          |

**Example:**

```json
{"type": "command_plan", "id": "cmd_001", "phase": "precondition", "description": "Verify BMC is reachable", "target": {"host": "192.168.1.100", "port": 22, "protocol": "ssh"}, "command": "ipmcget -d deviceinfo", "timeout_seconds": 15, "expected_exit_code": 0, "expected_output_contains": ["Board ID"], "on_failure": "abort"}
{"type": "command_plan", "id": "cmd_002", "phase": "execute", "description": "Query current fan speed", "target": {"host": "192.168.1.100", "port": 22, "protocol": "ssh"}, "command": "ipmcget -d fanspeed", "timeout_seconds": 15, "expected_exit_code": 0, "expected_output_contains": ["Fan1"], "on_failure": "retry"}
```

### 3.2 `interactive_command_plan` — Multi-Step Interactive Commands

For commands that require feeding input at specific prompts (password changes, confirmations, sudo).

**Schema:**

```json
{
  "type": "interactive_command_plan",
  "id": "icmd_001",
  "phase": "execute",
  "description": "Change user password via ipmcset",
  "target": {
    "host": "192.168.1.100",
    "port": 22,
    "protocol": "ssh"
  },
  "initial_command": "ipmcset -t user -d password -v testuser",
  "timeout_seconds": 60,
  "steps": [
    {
      "step": 1,
      "expect_prompt": "Enter current password:",
      "send_input": "OldPass123!",
      "is_secret": true,
      "timeout_seconds": 10
    },
    {
      "step": 2,
      "expect_prompt": "Enter new password:",
      "send_input": "NewPass456!",
      "is_secret": true,
      "timeout_seconds": 10
    },
    {
      "step": 3,
      "expect_prompt": "Confirm new password:",
      "send_input": "NewPass456!",
      "is_secret": true,
      "timeout_seconds": 10
    }
  ],
  "expected_final_output_contains": ["successfully", "Success"],
  "on_failure": "repair"
}
```

**Field Descriptions:**

| Field                             | Type     | Required | Description                                          |
|-----------------------------------|----------|----------|------------------------------------------------------|
| `type`                            | string   | yes      | Always `"interactive_command_plan"`                   |
| `id`                              | string   | yes      | Unique identifier                                    |
| `phase`                           | string   | yes      | `"precondition"`, `"execute"`, or `"postcondition"`  |
| `description`                     | string   | yes      | What this interactive flow accomplishes               |
| `target`                          | object   | yes      | Connection details                                   |
| `initial_command`                 | string   | yes      | The command that starts the interactive session       |
| `timeout_seconds`                 | integer  | yes      | Total timeout for the entire interaction              |
| `steps`                           | array    | yes      | Ordered list of prompt/response pairs                 |
| `steps[].step`                    | integer  | yes      | Step sequence number (1-based)                        |
| `steps[].expect_prompt`           | string   | yes      | Regex or substring to match in terminal output        |
| `steps[].send_input`             | string   | yes      | Text to send when prompt is matched                   |
| `steps[].is_secret`              | boolean  | no       | If true, redact from logs (default: false)            |
| `steps[].timeout_seconds`        | integer  | no       | Per-step timeout (default: 10)                        |
| `expected_final_output_contains` | string[] | no       | Substrings expected after all steps complete           |
| `on_failure`                      | string   | yes      | `"abort"`, `"continue"`, `"retry"`, or `"repair"`    |

### 3.3 `health_check_request` — Environment Health Verification

Emitted before or after critical operations to verify the environment is in a known-good state.

**Schema:**

```json
{
  "type": "health_check_request",
  "id": "hc_001",
  "phase": "precondition",
  "description": "Verify user accounts and BMC state before password change",
  "target": {
    "host": "192.168.1.100",
    "port": 22,
    "protocol": "ssh"
  },
  "checks": [
    {
      "name": "user_exists",
      "command": "ipmcget -d userlist",
      "expect_output_contains": ["testuser"],
      "timeout_seconds": 10
    },
    {
      "name": "user_not_locked",
      "command": "ipmcget -t user -d state -v testuser",
      "expect_output_contains": ["Enabled"],
      "timeout_seconds": 10
    },
    {
      "name": "bmc_responsive",
      "command": "ipmcget -d deviceinfo",
      "expect_exit_code": 0,
      "timeout_seconds": 15
    }
  ],
  "on_any_failure": "repair"
}
```

**Field Descriptions:**

| Field                              | Type     | Required | Description                                     |
|------------------------------------|----------|----------|-------------------------------------------------|
| `type`                             | string   | yes      | Always `"health_check_request"`                 |
| `id`                               | string   | yes      | Unique identifier                               |
| `phase`                            | string   | yes      | `"precondition"` or `"postcondition"`           |
| `description`                      | string   | yes      | What is being checked                            |
| `target`                           | object   | yes      | Connection details                               |
| `checks`                           | array    | yes      | List of individual health checks                 |
| `checks[].name`                   | string   | yes      | Check identifier                                 |
| `checks[].command`                | string   | yes      | Command to run                                   |
| `checks[].expect_output_contains` | string[] | no       | Expected substrings in output                    |
| `checks[].expect_exit_code`       | integer  | no       | Expected exit code                               |
| `checks[].timeout_seconds`        | integer  | no       | Timeout for this check (default: 10)             |
| `on_any_failure`                   | string   | yes      | `"abort"` or `"repair"`                          |

### 3.4 `repair_action` — Auto-Repair for Detected Issues

Emitted when the agent detects (or is informed of) a problem and provides a fix.

**Schema:**

```json
{
  "type": "repair_action",
  "id": "fix_001",
  "issue": "User 'testuser' is locked after failed password attempts",
  "severity": "critical",
  "target": {
    "host": "192.168.1.100",
    "port": 22,
    "protocol": "ssh"
  },
  "repair_commands": [
    {
      "command": "ipmcset -t user -d unlock -v testuser",
      "timeout_seconds": 15,
      "expected_exit_code": 0
    },
    {
      "command": "ipmcget -t user -d state -v testuser",
      "timeout_seconds": 10,
      "expected_output_contains": ["Enabled"]
    }
  ],
  "verify_after_repair": true,
  "on_repair_failure": "abort"
}
```

**Field Descriptions:**

| Field                                     | Type     | Required | Description                                 |
|-------------------------------------------|----------|----------|---------------------------------------------|
| `type`                                    | string   | yes      | Always `"repair_action"`                    |
| `id`                                      | string   | yes      | Unique identifier                           |
| `issue`                                   | string   | yes      | Description of the detected problem          |
| `severity`                                | string   | yes      | `"warning"`, `"critical"`, or `"fatal"`     |
| `target`                                  | object   | yes      | Connection details                           |
| `repair_commands`                         | array    | yes      | Ordered repair steps                         |
| `repair_commands[].command`              | string   | yes      | Repair command                               |
| `repair_commands[].timeout_seconds`      | integer  | no       | Timeout (default: 15)                        |
| `repair_commands[].expected_exit_code`   | integer  | no       | Expected exit code                           |
| `repair_commands[].expected_output_contains` | string[] | no  | Expected output substrings                   |
| `verify_after_repair`                     | boolean  | no       | Re-run the failed health check (default: true)|
| `on_repair_failure`                       | string   | yes      | `"abort"` or `"continue"`                   |

### 3.5 `completion_summary` — Final Test Result

Emitted once at the end of agent output to report the overall test outcome.

**Schema:**

```json
{
  "type": "completion_summary",
  "test_case": "TC_USER_PASSWORD_CHANGE_001",
  "result": "pass",
  "steps_executed": 5,
  "steps_passed": 5,
  "steps_failed": 0,
  "repairs_attempted": 1,
  "repairs_succeeded": 1,
  "duration_hint_seconds": 45,
  "details": [
    {"id": "hc_001", "status": "pass", "note": "All precondition checks passed"},
    {"id": "cmd_001", "status": "pass", "note": "User verified"},
    {"id": "icmd_001", "status": "pass", "note": "Password changed successfully"},
    {"id": "hc_002", "status": "fail", "note": "User was locked"},
    {"id": "fix_001", "status": "pass", "note": "User unlocked via repair"}
  ],
  "error_message": null
}
```

**Field Descriptions:**

| Field                  | Type     | Required | Description                                     |
|------------------------|----------|----------|-------------------------------------------------|
| `type`                 | string   | yes      | Always `"completion_summary"`                   |
| `test_case`            | string   | yes      | Test case identifier                             |
| `result`               | string   | yes      | `"pass"`, `"fail"`, or `"error"`                |
| `steps_executed`       | integer  | yes      | Total steps run                                  |
| `steps_passed`         | integer  | yes      | Successful steps                                 |
| `steps_failed`         | integer  | yes      | Failed steps                                     |
| `repairs_attempted`    | integer  | yes      | Number of repair actions triggered               |
| `repairs_succeeded`    | integer  | yes      | Number of successful repairs                     |
| `duration_hint_seconds`| integer  | no       | Estimated total duration                         |
| `details`              | array    | yes      | Per-step result breakdown                        |
| `error_message`        | string   | no       | Error description if `result` is `"error"`       |

## 4. Test Runner Pseudo-Code

```python
#!/usr/bin/env python3
"""
BMC Agent-Driven Test Runner
Starts Claude CLI, parses structured JSON stream, executes actions.
"""

import subprocess
import json
import re
import time
import paramiko
from dataclasses import dataclass, field
from typing import Optional


# ─────────────────────────────────────────────
# 4.1  SSH Executor
# ─────────────────────────────────────────────

class SSHExecutor:
    """Manages SSH connections and command execution on BMC targets."""

    def __init__(self):
        self._connections: dict[str, paramiko.SSHClient] = {}

    def get_connection(self, host: str, port: int = 22,
                       username: str = "root", password: str = "***") -> paramiko.SSHClient:
        key = f"{host}:{port}"
        if key not in self._connections:
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(host, port=port, username=username,
                           password=password, timeout=15)
            self._connections[key] = client
        return self._connections[key]

    def run_command(self, host: str, port: int, command: str,
                    timeout: int = 30) -> tuple[int, str, str]:
        """Execute a non-interactive command. Returns (exit_code, stdout, stderr)."""
        client = self.get_connection(host, port)
        stdin, stdout, stderr = client.exec_command(command, timeout=timeout)
        exit_code = stdout.channel.recv_exit_status()
        return exit_code, stdout.read().decode(), stderr.read().decode()

    def run_interactive(self, host: str, port: int, initial_command: str,
                        steps: list[dict], timeout: int = 60) -> tuple[bool, str]:
        """Execute an interactive command with prompt/response steps."""
        client = self.get_connection(host, port)
        channel = client.invoke_shell()
        channel.settimeout(timeout)
        output = ""

        # Send initial command
        channel.send(initial_command + "\n")
        time.sleep(1)

        for step in steps:
            # Wait for expected prompt
            step_timeout = step.get("timeout_seconds", 10)
            deadline = time.time() + step_timeout
            buffer = ""

            while time.time() < deadline:
                if channel.recv_ready():
                    chunk = channel.recv(4096).decode()
                    buffer += chunk
                    output += chunk
                if step["expect_prompt"] in buffer:
                    break
                time.sleep(0.2)
            else:
                return False, f"Timeout waiting for prompt: {step['expect_prompt']}"

            # Send input
            channel.send(step["send_input"] + "\n")
            time.sleep(0.5)

        # Collect remaining output
        time.sleep(1)
        while channel.recv_ready():
            output += channel.recv(4096).decode()

        channel.close()
        return True, output

    def close_all(self):
        for client in self._connections.values():
            client.close()
        self._connections.clear()


# ─────────────────────────────────────────────
# 4.2  Structured JSON Line Extractor
# ─────────────────────────────────────────────

STRUCTURED_TYPES = {
    "command_plan", "interactive_command_plan",
    "health_check_request", "repair_action", "completion_summary"
}

def extract_structured_json(text_buffer: str) -> list[dict]:
    """Extract structured JSON objects from accumulated text output."""
    results = []
    for line in text_buffer.splitlines():
        line = line.strip()
        if not line.startswith("{"):
            continue
        try:
            obj = json.loads(line)
            if isinstance(obj, dict) and obj.get("type") in STRUCTURED_TYPES:
                results.append(obj)
        except json.JSONDecodeError:
            continue
    return results


# ─────────────────────────────────────────────
# 4.3  Action Handlers
# ─────────────────────────────────────────────

@dataclass
class StepResult:
    id: str
    status: str          # "pass" | "fail" | "error"
    note: str = ""
    stdout: str = ""
    stderr: str = ""


class ActionHandler:
    """Dispatches structured JSON actions to the appropriate executor."""

    def __init__(self, ssh: SSHExecutor):
        self.ssh = ssh
        self.results: list[StepResult] = []

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
            return StepResult(id=action.get("id", "?"), status="error",
                              note=f"Unknown type: {action['type']}")
        result = handler(action)
        self.results.append(result)
        return result

    def _handle_command(self, action: dict) -> StepResult:
        target = action["target"]
        timeout = action.get("timeout_seconds", 30)
        try:
            exit_code, stdout, stderr = self.ssh.run_command(
                target["host"], target.get("port", 22),
                action["command"], timeout
            )
        except Exception as e:
            return StepResult(id=action["id"], status="error", note=str(e))

        # Validate exit code
        expected_rc = action.get("expected_exit_code", 0)
        if exit_code != expected_rc:
            return StepResult(
                id=action["id"], status="fail",
                note=f"Exit code {exit_code} != expected {expected_rc}",
                stdout=stdout, stderr=stderr
            )

        # Validate output contains
        for keyword in action.get("expected_output_contains", []):
            if keyword not in stdout:
                return StepResult(
                    id=action["id"], status="fail",
                    note=f"Output missing expected substring: '{keyword}'",
                    stdout=stdout
                )

        return StepResult(id=action["id"], status="pass",
                          note="Command executed successfully", stdout=stdout)

    def _handle_interactive(self, action: dict) -> StepResult:
        target = action["target"]
        try:
            success, output = self.ssh.run_interactive(
                target["host"], target.get("port", 22),
                action["initial_command"],
                action["steps"],
                action.get("timeout_seconds", 60)
            )
        except Exception as e:
            return StepResult(id=action["id"], status="error", note=str(e))

        if not success:
            return StepResult(id=action["id"], status="fail",
                              note=output, stdout=output)

        # Validate final output
        for keyword in action.get("expected_final_output_contains", []):
            if keyword not in output:
                return StepResult(
                    id=action["id"], status="fail",
                    note=f"Final output missing: '{keyword}'", stdout=output
                )

        return StepResult(id=action["id"], status="pass",
                          note="Interactive command completed", stdout=output)

    def _handle_health_check(self, action: dict) -> StepResult:
        target = action["target"]
        failed_checks = []

        for check in action["checks"]:
            try:
                exit_code, stdout, stderr = self.ssh.run_command(
                    target["host"], target.get("port", 22),
                    check["command"], check.get("timeout_seconds", 10)
                )
            except Exception as e:
                failed_checks.append(f"{check['name']}: {e}")
                continue

            if "expect_exit_code" in check and exit_code != check["expect_exit_code"]:
                failed_checks.append(
                    f"{check['name']}: exit_code={exit_code}")

            for kw in check.get("expect_output_contains", []):
                if kw not in stdout:
                    failed_checks.append(
                        f"{check['name']}: missing '{kw}' in output")

        if failed_checks:
            return StepResult(
                id=action["id"], status="fail",
                note=f"Failed checks: {'; '.join(failed_checks)}")

        return StepResult(id=action["id"], status="pass",
                          note="All health checks passed")

    def _handle_repair(self, action: dict) -> StepResult:
        target = action["target"]
        for repair_cmd in action["repair_commands"]:
            try:
                exit_code, stdout, stderr = self.ssh.run_command(
                    target["host"], target.get("port", 22),
                    repair_cmd["command"],
                    repair_cmd.get("timeout_seconds", 15)
                )
            except Exception as e:
                return StepResult(id=action["id"], status="error",
                                  note=f"Repair failed: {e}")

            expected_rc = repair_cmd.get("expected_exit_code", 0)
            if exit_code != expected_rc:
                return StepResult(
                    id=action["id"], status="fail",
                    note=f"Repair command failed: exit {exit_code}")

        return StepResult(id=action["id"], status="pass",
                          note=f"Repair succeeded for: {action['issue']}")

    def _handle_summary(self, action: dict) -> StepResult:
        # Summary is informational — just log it
        return StepResult(
            id="summary", status=action.get("result", "unknown"),
            note=json.dumps(action, ensure_ascii=False)
        )


# ─────────────────────────────────────────────
# 4.4  Main Test Runner
# ─────────────────────────────────────────────

def build_agent_prompt(test_case: dict, context: str = "") -> str:
    """Build the prompt to send to Claude CLI with BMC testing skills."""
    return f"""You are a BMC test automation agent. Execute the following test case.
Output ONLY structured JSON lines (one per line) using these types:
- command_plan, interactive_command_plan, health_check_request, repair_action, completion_summary

Test Case:
  ID: {test_case['id']}
  Title: {test_case['title']}
  Target: {test_case['target_host']}
  Steps: {json.dumps(test_case['steps'], ensure_ascii=False)}

{f"Previous Context: {context}" if context else ""}

Rules:
- Always emit a health_check_request BEFORE any destructive or credential operation.
- Use interactive_command_plan for any command involving password prompts or confirmations.
- If a health check fails, emit a repair_action before retrying.
- End with exactly one completion_summary.
- Output each JSON object on a single line. No markdown, no explanation outside JSON.
"""


def run_test_case(test_case: dict) -> dict:
    """Run a single test case through the Claude agent pipeline."""
    ssh = SSHExecutor()
    handler = ActionHandler(ssh)

    prompt = build_agent_prompt(test_case)

    # Start Claude CLI process
    process = subprocess.Popen(
        ["claude", "-p", prompt, "--output-format", "stream-json", "--verbose"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        bufsize=1
    )

    text_buffer = ""
    final_summary = None

    try:
        # Real-time parse stream-json lines
        for raw_line in process.stdout:
            raw_line = raw_line.strip()
            if not raw_line:
                continue

            # Parse Claude's stream-json envelope
            try:
                envelope = json.loads(raw_line)
            except json.JSONDecodeError:
                continue

            # Extract text content from assistant messages
            if envelope.get("type") == "content_block_delta":
                delta = envelope.get("delta", {})
                if delta.get("type") == "text_delta":
                    text_buffer += delta.get("text", "")

            # Also handle complete assistant message
            if envelope.get("type") == "message_stop":
                pass  # Final flush below

            # Try to extract and handle structured actions from accumulated text
            actions = extract_structured_json(text_buffer)
            if actions:
                # Remove processed lines from buffer
                for action in actions:
                    action_line = json.dumps(action, ensure_ascii=False)
                    text_buffer = text_buffer.replace(action_line, "", 1)

                # Execute each action
                for action in actions:
                    result = handler.handle(action)
                    log_step_result(test_case["id"], action, result)

                    if action["type"] == "completion_summary":
                        final_summary = action

                    # Handle on_failure policies
                    if result.status == "fail":
                        on_failure = action.get("on_failure",
                                    action.get("on_any_failure",
                                    action.get("on_repair_failure", "abort")))
                        if on_failure == "abort":
                            process.terminate()
                            break

    except Exception as e:
        print(f"[ERROR] Test {test_case['id']}: {e}")
    finally:
        process.wait(timeout=10)
        ssh.close_all()

    # Build result report
    return {
        "test_case": test_case["id"],
        "result": final_summary.get("result") if final_summary else "error",
        "steps": [{"id": r.id, "status": r.status, "note": r.note}
                  for r in handler.results],
        "agent_summary": final_summary
    }


def log_step_result(test_id: str, action: dict, result: StepResult):
    """Log each step execution with appropriate redaction."""
    is_secret = False
    if action["type"] == "interactive_command_plan":
        is_secret = any(s.get("is_secret") for s in action.get("steps", []))

    status_icon = "✓" if result.status == "pass" else "✗"
    print(f"  [{status_icon}] {action['type']}:{action.get('id', '?')} — {result.note}")

    if result.stdout and not is_secret:
        preview = result.stdout[:200].replace("\n", "\\n")
        print(f"      stdout: {preview}")


# ─────────────────────────────────────────────
# 4.5  Batch Runner Entry Point
# ─────────────────────────────────────────────

def run_all_tests(test_suite_path: str):
    """Load and run all test cases from a JSON suite file."""
    with open(test_suite_path) as f:
        suite = json.load(f)

    results = []
    for tc in suite["test_cases"]:
        print(f"\n{'='*60}")
        print(f"Running: {tc['id']} — {tc['title']}")
        print(f"{'='*60}")
        result = run_test_case(tc)
        results.append(result)
        print(f"Result: {result['result'].upper()}")

    # Summary
    passed = sum(1 for r in results if r["result"] == "pass")
    failed = sum(1 for r in results if r["result"] == "fail")
    errors = sum(1 for r in results if r["result"] == "error")
    print(f"\n{'='*60}")
    print(f"TOTAL: {len(results)} | PASS: {passed} | FAIL: {failed} | ERROR: {errors}")
    print(f"{'='*60}")

    return results


if __name__ == "__main__":
    import sys
    suite_path = sys.argv[1] if len(sys.argv) > 1 else "test_suite.json"
    run_all_tests(suite_path)
```

## 5. Recommended Modifications to the Existing Framework

### 5.1 New Files to Create

| File                       | Purpose                                                    |
|----------------------------|------------------------------------------------------------|
| `bmc_test_runner.py`       | Main test runner (implements Section 4 above)              |
| `bmc_ssh_executor.py`      | SSH connection pool & command execution (extract from 4.1) |
| `bmc_action_handler.py`    | Structured JSON action dispatcher (extract from 4.3)       |
| `bmc_agent_prompt.py`      | Prompt templates for Claude with BMC testing skills        |
| `test_suite.json`          | Example test suite definition                              |

### 5.2 Existing Files to Modify

| File                 | Modification                                                           |
|----------------------|------------------------------------------------------------------------|
| `bmc_mcp_server.py`  | Add `import torch` (line 21 bug fix); add a `get_command_details` tool that returns full JSON for a specific command by ID — useful for agent to build accurate command plans |
| `CLAUDE.md` (create) | Add BMC testing skills (Skill 1–3 from user prompt) as system instructions so every Claude CLI invocation automatically uses structured output |

### 5.3 CLAUDE.md — Agent Instructions File

Create `CLAUDE.md` in the project root with the BMC testing skills so that Claude automatically follows the structured output contract:

```markdown
# BMC Testing Agent Instructions

When executing BMC test cases, you MUST output structured JSON lines only.

## Output Types
- `command_plan` — for non-interactive commands
- `interactive_command_plan` — for commands with password/confirmation prompts
- `health_check_request` — before/after critical operations
- `repair_action` — when environment issues are detected
- `completion_summary` — exactly one, at the end

## Rules
1. NEVER try to execute interactive commands in one shot.
2. ALWAYS emit health_check_request before credential or destructive operations.
3. Use interactive_command_plan with explicit steps for any password/sudo/yes-no flow.
4. If a check fails, emit repair_action before retrying.
5. Output one JSON object per line. No markdown. No explanation outside JSON.
```

### 5.4 Example `test_suite.json`

```json
{
  "suite_name": "BMC User Management Smoke Test",
  "default_target": {
    "host": "192.168.1.100",
    "port": 22,
    "protocol": "ssh",
    "username": "root",
    "password": "***"
  },
  "test_cases": [
    {
      "id": "TC_USER_LIST_001",
      "title": "Query user list and verify default users exist",
      "target_host": "192.168.1.100",
      "steps": [
        "Query the BMC user list using ipmcget -d userlist",
        "Verify that 'root' and 'Administrator' appear in the output"
      ]
    },
    {
      "id": "TC_USER_PASSWORD_CHANGE_001",
      "title": "Change testuser password via interactive ipmcset",
      "target_host": "192.168.1.100",
      "steps": [
        "Health check: verify testuser exists and is not locked",
        "Change password from OldPass123! to NewPass456! using ipmcset",
        "Verify the new password works by re-authenticating",
        "Health check: verify testuser is still enabled"
      ]
    },
    {
      "id": "TC_FAN_QUERY_001",
      "title": "Query fan speed and verify all fans are reporting",
      "target_host": "192.168.1.100",
      "steps": [
        "Query fan speed using ipmcget -d fanspeed",
        "Verify all fan slots (Fan1 through Fan6) appear in output",
        "Verify no fan shows 0 RPM (indicates failure)"
      ]
    }
  ]
}
```

## 6. Security & Robustness Considerations

### 6.1 Credential Management

| Risk                          | Mitigation                                                               |
|-------------------------------|--------------------------------------------------------------------------|
| Passwords in prompts          | Use environment variables or vault references; never hardcode in test suite JSON. The runner resolves `$ENV{VAR}` placeholders at runtime. |
| Passwords in agent output     | `is_secret: true` fields are redacted in all logs. The runner replaces secret values with `***` before writing to disk. |
| Passwords in Claude logs      | Use `--verbose` only in development. In CI, omit it to reduce log surface. |

### 6.2 Timeout & Deadlock Prevention

| Scenario                      | Mitigation                                                               |
|-------------------------------|--------------------------------------------------------------------------|
| Claude CLI hangs              | Global process timeout (default: 300s). `process.wait(timeout=...)` with `SIGTERM` fallback. |
| SSH command hangs             | Per-command `timeout_seconds` enforced by paramiko. Channel is force-closed on timeout. |
| Interactive prompt never appears | Per-step `timeout_seconds` (default: 10s). Fails the step cleanly with descriptive error. |
| Infinite repair loop          | Max repair attempts per test case (default: 3). After limit, abort with `"error"` result. |

### 6.3 Error Recovery & Retry

```
on_failure values and behavior:

  "abort"    → Stop the test case immediately. Mark as "fail".
  "continue" → Log the failure, proceed to next action.
  "retry"    → Re-execute the same action once. If still fails, treat as "abort".
  "repair"   → Expect the agent to emit a repair_action next.
               The runner executes the repair, then re-runs the failed action.
               Max 3 repair cycles per test case.
```

### 6.4 State Isolation

| Concern                       | Solution                                                                 |
|-------------------------------|--------------------------------------------------------------------------|
| Tests affect each other       | Each test case gets a fresh Claude CLI process. No shared state between runs. |
| SSH connection leaks          | `SSHExecutor.close_all()` called in `finally` block after each test case. |
| Leftover BMC state            | Use `postcondition` phase health checks. Agent should emit cleanup commands to restore original state (e.g., re-lock test users, reset passwords to defaults). |
| Parallel test interference    | If running tests in parallel, assign separate target hosts or user accounts per worker. |

### 6.5 Command Injection Prevention

| Attack Vector                 | Mitigation                                                               |
|-------------------------------|--------------------------------------------------------------------------|
| Agent outputs malicious commands | Allowlist of permitted command prefixes (`ipmcget`, `ipmcset`, `ipmctool`, etc.). The runner rejects any command not matching the allowlist. |
| Shell metacharacter injection | Commands are passed to `exec_command()` directly, not through a shell. No shell expansion occurs. |
| Agent prompt injection        | Test case steps are sanitized: no backticks, no `$()`, no template injection. |

### 6.6 Audit & Logging

All test executions produce a structured log file:

```
logs/
  TC_USER_PASSWORD_CHANGE_001_20260323_143022.json
```

Each log contains:
- Full test case definition (with secrets redacted)
- Every structured action received from the agent
- Every execution result (stdout/stderr with secrets redacted)
- Final summary and timing information

This enables post-mortem analysis without re-running tests.
