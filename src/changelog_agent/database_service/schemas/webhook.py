from pydantic import BaseModel, ConfigDict

class WebhookCreate(BaseModel):
    webhook_id: str
    webhook_event: str
    repo_name: str
    author: str

class WebhookResponse(BaseModel):
    webhook_id: str
    webhook_event: str
    repo_name: str
    author: str

    model_config = ConfigDict(from_attributes=True)





