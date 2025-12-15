from pydantic import BaseModel
from typing import Literal


class ClassificationResult(BaseModel):
    comment_sha: str
    type: Literal['feature', 'fix', 'chore', 'docs', 'refactor']
    scope: str
    breaking_change: bool
    confidence: float


"""
- "feature": introduces new user-facing functionality
- "fix": bug fix
- "chore": maintenance, tooling, CI
- "docs": documentation only
- "refactor": code restructuring without behavior change
"""



