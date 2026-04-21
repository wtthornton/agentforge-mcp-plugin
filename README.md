# agentforge-mcp-plugin

Test rig for AgentForge MCP server validation (TAP-768).

Exercises `AgentLoader.load_external()` with two agents that differ only in their `mcp_servers` declaration:

| Agent | `mcp_servers` | Expected outcome |
|---|---|---|
| `known-mcp-agent` | `["tapps-brain"]` | Loads cleanly, resolvable via namespace registry |
| `bad-mcp-agent` | `["nonexistent-server-xyz"]` | Silently rejected at load time (`UnknownMCPServerError` caught by `_scan_directory`) |

## Install

```bash
cd /path/to/AgentForge
uv pip install -e /path/to/agentforge-mcp-plugin
```

## Run smoke tests

```bash
uv run pytest backend/tests/test_mcp_smoke.py -v
```

Tests are skipped automatically when the package is not installed.

## Structure

```
agentforge_mcp_test/
  __init__.py          # __version__ = "1.0.0"
  plugin.json          # plugin manifest
  plugin.py            # register(app) — mounts router
  routes.py            # GET /api/mcp-test/status
  agents/
    known_mcp_agent/
      AGENT.md         # mcp_servers: ["tapps-brain"]
      runner.py        # KnownMCPRunner.run() -> "known-mcp:ok"
    bad_mcp_agent/
      AGENT.md         # mcp_servers: ["nonexistent-server-xyz"]
      runner.py        # BadMCPRunner.run() -> "bad-mcp:ok" (never reached)
tests/
  test_runners.py      # unit tests for runner classes (no AgentForge dep)
backend/tests/
  test_mcp_smoke.py    # integration smoke test (lives in AgentForge repo)
```
