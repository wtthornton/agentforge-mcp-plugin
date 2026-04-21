"""Plugin entry point — registers routes and loads both test agents."""

from __future__ import annotations

from fastapi import FastAPI

from agentforge_mcp_test.routes import router


def register(app: FastAPI) -> None:
    """Mount the mcp-test router onto *app*."""
    app.include_router(router)
