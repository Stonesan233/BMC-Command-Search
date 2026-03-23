# bmc_agent_external

Standalone components for unattended, streaming-JSON-based BMC testing with Claude Code CLI. Everything here can be built and tested without access to the closed-source internal framework.

## Directory Layout

```
bmc_agent_external/
├── CLAUDE.md                          # Agent system prompt (auto-loaded by Claude CLI)
├── schemas/
│   └── bmc_action_schemas.json        # JSON Schema Draft 2020-12 for all action types
├── runner/
│   └── stream_parser.py               # DeltaAccumulator + InteractiveSession state machine
├── ssh/
│   └── interactive_executor.py        # Pexpect-style SSH executor + MockChannel for testing
├── examples/
│   └── test_password_change.json      # Sample test case definition
└── README.md
```

## Quick Start

### 1. Verify the mock self-test works

```bash
cd bmc_agent_external
python -m ssh.interactive_executor
# Expected: "SELF-TEST PASSED"
```

This runs a scripted password-change flow using `MockChannel` — no hardware, no SSH.

### 2. Test the stream parser

```python
from runner.stream_parser import DeltaAccumulator

acc = DeltaAccumulator()

# Simulate fragmented deltas (as Claude CLI emits them)
acc.feed('{"type":"command_plan","id":"cmd_001","phase":"pre')
acc.feed('condition","description":"Check BMC","target":{"host":"1.2.3.4",')
acc.feed('"port":22,"protocol":"ssh"},"command":"ipmcget -d deviceinfo",')
acc.feed('"timeout_seconds":15,"expected_exit_code":0,')
acc.feed('"expected_output_contains":["Board ID"],"on_failure":"abort"}\n')

actions = acc.extract_actions()
assert len(actions) == 1
assert actions[0]["type"] == "command_plan"
print("Stream parser OK:", actions[0]["id"])
```

### 3. Test schema validation

```bash
pip install jsonschema
python -c "
import json, jsonschema

with open('schemas/bmc_action_schemas.json') as f:
    schema = json.load(f)

# Valid action
action = {
    'type': 'command_plan', 'id': 'cmd_001', 'phase': 'precondition',
    'description': 'Check BMC reachability', 'target': {'host': '1.2.3.4', 'port': 22, 'protocol': 'ssh'},
    'command': 'ipmcget -d deviceinfo', 'timeout_seconds': 15,
    'expected_exit_code': 0, 'expected_output_contains': ['Board ID'],
    'on_failure': 'abort',
}
jsonschema.validate(action, schema)
print('Schema validation PASSED')
"
```

### 4. Integration with a real runner

Your test runner would wire these components together:

```python
import subprocess
from runner.stream_parser import parse_stream_lines, StepResult
from ssh.interactive_executor import InteractiveCommandRunner

process = subprocess.Popen(
    ["claude", "-p", prompt, "--output-format", "stream-json"],
    stdout=subprocess.PIPE, text=True, bufsize=1,
)

context = ""
for action in parse_stream_lines(process.stdout):
    if action["type"] == "command_plan":
        # ssh.exec_command(action["command"], ...)
        pass
    elif action["type"] == "interactive_command_plan":
        runner = InteractiveCommandRunner(ssh_client)
        ok, output = runner.run_steps(
            action["initial_command"], action["steps"]
        )
        runner.close()
    elif action["type"] == "completion_summary":
        context = action.get("next_context_summary", "")
```

## Key Design Decisions

| Decision | Rationale |
|----------|-----------|
| `DeltaAccumulator` buffers by newline | Claude's `text_delta` splits at arbitrary byte boundaries; naive `splitlines()` on each delta yields broken JSON |
| `InteractiveSession` is a state machine | Explicit states (`WAITING_PROMPT` / `SENDING_INPUT` / `COLLECTING_TAIL`) replace fragile `time.sleep()` polling |
| `next_context_summary` in `completion_summary` | Enables cross-case context chaining — the runner injects it into the next test case's prompt |
| `$ENV{VAR}` placeholders for secrets | Passwords never appear in test definitions or agent output; resolved at runtime by the runner |
| `MockChannel` / `MockSSHClient` | Full interactive-flow testing without hardware or SSH connectivity |

## Dependencies

- **Required**: Python 3.10+
- **Optional**: `paramiko` (for real SSH), `jsonschema` (for schema validation)
- **For testing**: None (MockChannel is self-contained)
