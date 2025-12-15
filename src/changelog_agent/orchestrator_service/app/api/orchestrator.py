
from fastapi import APIRouter
from src.changelog_agent.orchestrator_service.app.schemas.orchestrator_input import OrchestratorInput
from src.changelog_agent.orchestrator_service.app.services.classifier_agent import run_classifier

from src.changelog_agent.utils.exception_config import ProjectException
from src.changelog_agent.utils.logger_config import log
from src.changelog_agent.classifier_service.app.agent.classification_agent import classify_commits

router = APIRouter()

@router.post('/start')
async def start(payload: OrchestratorInput):
    """
    Entry point for all webhook driven workflows
    """

    print("Orchestrator received payload")
    print(payload.model_dump())
    print(payload.commits)

    # later:
    # - call classifier agent

    # - call summarizer agent

    # - store to DB

    # - trigger notifications

    try:
        if not payload.commits:
            raise ValueError('No commits received')

        # classification
        log.info("--- Running classifier agent ---")
        classifications = run_classifier(payload.commits)
        print(classifications)

        return {
            'statusCode': 200,
            'status': 'success',
            'classification': classifications
        }

    except Exception as e:
        ProjectException(
            e,
            context={
                'operation': 'start',
                'message': 'An error occurred',
            }
        )

