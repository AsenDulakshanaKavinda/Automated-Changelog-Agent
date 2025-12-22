
from pydantic import BaseModel
""" Webhook input schema """

class WebhookInput(BaseModel):
    webhook_id: str
    webhook_event: str
    repo_name: str
    author: str