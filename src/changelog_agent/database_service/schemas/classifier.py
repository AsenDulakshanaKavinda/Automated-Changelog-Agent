from pydantic import BaseModel, ConfigDict
from typing import Literal

class ClassifierCreat(BaseModel):
    comment_sha: str
    type: Literal['feature', 'fix', 'chore', 'docs', 'refactor']
    message: str
    scope: str
    breaking_change: bool
    confidence: float
    files_changed: list[str]

class ClassifierResponse(BaseModel):
    comment_sha: str
    type: str
    confidence: str

    model_config = ConfigDict(from_attributes=True)

