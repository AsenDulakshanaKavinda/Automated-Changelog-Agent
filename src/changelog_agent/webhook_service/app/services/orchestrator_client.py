
import requests
from src.changelog_agent.webhook_service.app.schemas.orchestrator_input import OrchestratorInput

ORCHESTRATOR_URL = "http://localhost:8003/orchestrator/start"


def send_to_orchestrator(payload: OrchestratorInput):
    """
    Sending a JSON payload to a specific URL(ORCHESTRATOR_URL) via an HTTP POST request

    Args:
        payload (OrchestratorInput): The payload to send to a specific URL
    """

    # send a POST request to the defined URL
    response = requests.post(ORCHESTRATOR_URL, json=payload)
    response.raise_for_status()


