
"""
- Release Service
    - acts as the Release agent of the Changelog Agent System.
    - receives summerized commits from the summarizer service.
    - then create the release note
    - forwards structured release note data to the Orchestrator Service for further processing.
"""

# ===============================
# Release Service Metadata
# ===============================
__version__="0.1.0"
__author__="Asen Dulakshana"
__email__=""
__description__ = (
    "Release service for the Changelog Agent System. "
    "Receives summarized commits and metadata from the summarizer service. ,"
    "and forwards structured release data inputs to the Orchestrator Service."
)

# ===============================
# Release Service Metadata
# ===============================

from src.changelog_agent.release_service.app.agent.release_manager_agent import release_manager
from src.changelog_agent.release_service.app.prompt.release_prompt import release_manager_prompt
from src.changelog_agent.release_service.app.schemas.schema import ReleaseManagerOutput
from src.changelog_agent.release_service.app.schemas.parser import release_manager_parser

__all__ = [
    'release_manager',
    'release_manager_prompt',
    'release_manager_parser',
    'ReleaseManagerOutput',
]