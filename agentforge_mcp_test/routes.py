"""Status route for the mcp-test plugin."""

from __future__ import annotations

from fastapi import APIRouter

from agentforge_mcp_test import __version__

router = APIRouter(prefix="/api/mcp-test", tags=["mcp-test"])


@router.get("/status")
async def status() -> dict:
    return {"status": "ok", "plugin": "mcp-test", "version": __version__}
