
import requests

from src.database.app.schemas.schema import WebhookTableSchema

""" DB_URL = 'http://localhost:8004/database/start'

def send_to_db(webhook_tbl_input: WebhookTableSchema):

    response = requests.post(DB_URL, json=webhook_tbl_input)
    response.raise_for_status() """


import requests
import json
from typing import Any

DB_URL = "http://localhost:8004/database/start"

def send_to_db(payload: dict[str, Any]) -> None:
    """
    Send payload to the database service. Use requests.json so FastAPI receives proper JSON.
    """
    headers = {"Content-Type": "application/json"}
    response = requests.post(DB_URL, json=payload, headers=headers, timeout=10)
    if response.status_code == 422:
        # helpful debug output for validation errors
        raise RuntimeError(f"DB rejected payload (422): {response.text}")
    response.raise_for_status()




