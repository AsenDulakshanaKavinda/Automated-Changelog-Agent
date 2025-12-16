from pydantic import BaseModel
from typing import List

class SummarizerResults(BaseModel):
    comment_sha: str
    summary: str