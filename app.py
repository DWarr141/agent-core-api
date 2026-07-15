"""Agent Core API.

This API provides a RESTful interface for managing agents and tasks.
"""

from fastapi import FastAPI

from src.config.settings import settings
from src.routes.chat import router as chat_router

app = FastAPI(
    title=settings.api_name,
    version=settings.api_version,
    debug=settings.debug,
)

app.include_router(chat_router)


@app.get("/health")
async def health_check() -> dict[str, str]:
    """Verify the operational status of the API application layers."""
    return {
        "status": "ok",
        "version": settings.api_version,
        "environment": settings.app_env,
        "debug": str(settings.debug),
    }
