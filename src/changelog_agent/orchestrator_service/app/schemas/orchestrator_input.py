
from pydantic import BaseModel
from typing import List, Optional

""" Orchestrator input schema """

class Commit(BaseModel):
    sha: str
    message: str
    author: str
    timestamp: str
    file_changed: List[str]


class OrchestratorInput(BaseModel):
    event_type: str
    # repo_id: str
    repo_name: str
    branch: Optional[str]
    commits: Optional[List[Commit]]
    pull_request: Optional[dict]
    metadata: dict
