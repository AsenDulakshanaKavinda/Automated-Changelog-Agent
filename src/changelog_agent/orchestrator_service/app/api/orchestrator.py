
from fastapi import APIRouter, BackgroundTasks
from src.changelog_agent.orchestrator_service.app.schemas.orchestrator_input import OrchestratorInput
from src.changelog_agent.orchestrator_service.app.background_tasks.tasks import run_orchestration

from src.changelog_agent.utils.exception_config import ProjectException
from src.changelog_agent.utils.logger_config import log

router = APIRouter()

@router.post('/start')
async def start(payload: OrchestratorInput, background_tasks: BackgroundTasks):
    """
    Entry point for all webhook driven workflows
    """

    log.info("Webhook received from GitHub")

    try:

        # schedule background processing
        background_tasks.add_task(run_orchestration, payload)

        return {
            "status": "accepted",
            'message': 'payload received and processing started'
        }

    except Exception as e:
        ProjectException(
            e,
            context={
                'operation': 'start',
            }
        )







