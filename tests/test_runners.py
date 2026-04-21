"""Unit tests for KnownMCPRunner and BadMCPRunner."""

from agentforge_mcp_test.agents.known_mcp_agent.runner import KnownMCPRunner
from agentforge_mcp_test.agents.bad_mcp_agent.runner import BadMCPRunner


def test_known_mcp_runner_returns_sentinel() -> None:
    assert KnownMCPRunner().run() == "known-mcp:ok"


def test_bad_mcp_runner_returns_sentinel() -> None:
    # Runner itself is functional — it's the loader that rejects the agent.
    assert BadMCPRunner().run() == "bad-mcp:ok"
