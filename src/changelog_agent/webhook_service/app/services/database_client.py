import requests
from src.changelog_agent.webhook_service.app.schemas.webhook_input import WebhookInput

DATABASE_URL = "http://localhost:8000/webhook/start"


def send_to_database(payload: WebhookInput):
    """
    Sending a JSON payload to a specific URL(DATABASE_URL) via an HTTP POST request

    Args:
        payload (DATABASE_URL): The payload to send to a specific URL
    """

    # send a POST request to the defined URL
    response = requests.post(DATABASE_URL, json=payload)
    response.raise_for_status()
