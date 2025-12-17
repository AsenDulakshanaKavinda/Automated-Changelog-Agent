from pydantic import BaseModel, Field
from typing import Literal, Optional, List
from enum import Enum

class ReleaseReadinessStatus(str, Enum):
    READY = "ready"
    READY_WITH_WARNINGS = "ready_with_warnings"
    NOT_READY = "not_ready"

class ReleaseSection(BaseModel):
    title: str = Field(..., description="Section title such as 'New Features', 'Bug Fixes', or 'Breaking Changes'")
    items: List[str] = Field(..., description="List of summarized bullet points for this section")

class ReleaseNote(BaseModel):
    title: str = Field(..., description="Release title, usually including veesion number")
    overview: str = Field(..., description="High level summary describing the main themes of this release")
    sections: List[ReleaseSection] = Field(..., description="Grouped release sections contained in this section")

class ReleaseReadiness(BaseModel):
    status: ReleaseReadinessStatus = Field(..., description="Overall readiness decision for the release")
    explanation: str = Field(..., description="Short explanation justifying the readiness decision")

class ReleaseManagerOutput(BaseModel):
    release_notes: ReleaseNote = Field(..., description="Final composed release notes")
    readiness: ReleaseReadiness = Field(..., description="Release readiness evaluation")
    risks: Optional[List[str]] = Field(None, description="Optional list of identified risks or concerns")
    audience: Optional[str] = Field(None, description="Suggested audience for this release (e.g. public, internal, developers)")
    display_message: str = Field(..., description="Message displayed for this release as a markdown")






