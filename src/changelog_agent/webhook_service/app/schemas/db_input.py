from datetime import datetime
from pydantic import BaseModel
from typing import Optional, Dict, Any


class WebhookTableSchema(BaseModel):
    webhook_id: str
    webhook_event: str
    repo_name: str
    branch: Optional[str]
    author: Optional[str]
    # timestamp: Optional[str | datetime]
    # payload: Dict