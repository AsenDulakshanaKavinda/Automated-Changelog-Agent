
import requests

from src.database.app.schemas.schema import WebhookTableSchema

DB_URL = 'http://localhost:8004/webhook'

def send_to_db(webhook_tbl_input: WebhookTableSchema):

    response = requests.post(DB_URL, json=webhook_tbl_input)
    response.raise_for_status()







