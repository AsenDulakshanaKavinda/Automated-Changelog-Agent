
from fastapi import APIRouter
from src.changelog_agent.orchestrator_service import OrchestratorInput


router = APIRouter()

@router.post('/start')
async def start(payload: OrchestratorInput):
    """
    Entry point for all webhook driven workflows
    """

    print("Orchestrator received payload")
    print(payload.model_dump())

    # later:
    # - call classifier agent
    # - call summarizer agent
    # - store to DB
    # - trigger notifications

    return {'status': 'orchestrator started'}
