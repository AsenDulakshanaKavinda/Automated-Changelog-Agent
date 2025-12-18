from datetime import datetime
from pydantic import BaseModel
from typing import Optional, Dict, Any


class WebhookTableSchema(BaseModel):
    webhook_id: str
    webhook_event: str
    repo_name: Optional[str]
    branch: Optional[str]
    author: Optional[str]
    timestamp: str
    payload: Dict[str, Any]