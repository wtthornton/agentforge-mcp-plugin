"""Runner for known-mcp-agent — always succeeds (MCP server is valid)."""

from __future__ import annotations


class KnownMCPRunner:
    """Deterministic runner that returns a fixed success sentinel."""

    def run(self, *args: object, **kwargs: object) -> str:
        return "known-mcp:ok"
