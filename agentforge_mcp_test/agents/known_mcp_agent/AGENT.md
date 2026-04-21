---
name: known-mcp-agent
namespace: project.mcp-test.known-mcp-agent
description: Test agent declaring a known MCP server — should load cleanly.
keywords: [mcp, test]
mcp_servers: ["tapps-brain"]
runner: agentforge_mcp_test.agents.known_mcp_agent.runner:KnownMCPRunner
---
