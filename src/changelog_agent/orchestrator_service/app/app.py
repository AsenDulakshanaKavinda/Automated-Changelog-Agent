from fastapi import FastAPI

from src.changelog_agent.orchestrator_service.app.api.orchestrator import router

app = FastAPI(title="Orchestrator", description="Orchestrator Service")

app.include_router(
    router,
    prefix="/orchestrator",
    tags=["Orchestrator"],
)

