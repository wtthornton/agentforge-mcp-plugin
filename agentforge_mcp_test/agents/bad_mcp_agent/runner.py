"""Runner for bad-mcp-agent — declares a nonexistent MCP server.

This runner is never invoked in practice: the loader rejects the agent at
load time due to the unknown MCP server name, so this file exists solely
to make the package importable and to document the intent.
"""

from __future__ import annotations


class BadMCPRunner:
    """Runner that should never be reached — agent is rejected at load time."""

    def run(self, *args: object, **kwargs: object) -> str:
        return "bad-mcp:ok"
