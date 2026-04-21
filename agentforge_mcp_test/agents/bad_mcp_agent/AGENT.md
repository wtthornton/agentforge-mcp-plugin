---
name: bad-mcp-agent
namespace: project.mcp-test.bad-mcp-agent
description: Test agent declaring an unknown MCP server — should fail validation.
keywords: [mcp, test, invalid]
mcp_servers: ["nonexistent-server-xyz"]
runner: agentforge_mcp_test.agents.bad_mcp_agent.runner:BadMCPRunner
---
