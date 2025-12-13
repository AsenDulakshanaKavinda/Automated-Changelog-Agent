
import requests

ORCHESTRATOR_URL = "ORCHESTRATOR_URL"


def send_to_orchestrator(payload: dict):
    """
    Sending a JSON payload to a specific URL(ORCHESTRATOR_URL) via an HTTP POST request
    """

    # send a POST request to the defined URL
    response = requests.post(ORCHESTRATOR_URL, json=payload, timeout=5)
    response.raise_for_status()








