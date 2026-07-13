"""Agent Core API.

This API provides a RESTful interface for managing agents and tasks.
"""

from fastapi import FastAPI

from src.services.agents import router as agents_router
from src.services.tasks import router as tasks_router

app = FastAPI(title="Agent Core API")

app.include_router(agents_router)
app.include_router(tasks_router)


@app.get("/health")
async def health_check() -> dict[str, str]:
    """Verify the operational status of the API application layers."""
    return {"status": "ok", "version": "1.0.0"}
