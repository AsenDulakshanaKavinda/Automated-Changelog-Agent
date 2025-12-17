
"""
- Summarizer Service
    - acts as the commit summerization agent of the Changelog Agent System.
    - receives classified commits from the classification service.
    - then summerize the commit
    - forwards structured summerized data to the Orchestrator Service for further processing (release service).
"""

# ===============================
# Summarizer Service Metadata
# ===============================
__version__="0.1.0"
__author__="Asen Dulakshana"
__email__=""
__description__ = (
    "Summarizer service for the Changelog Agent System. "
    "Receives classified commits and metadata from the classification service. ,"
    "and forwards structured summarized inputs to the Orchestrator Service."
)

# ===============================
# Summarizer Service Metadata
# ===============================

from src.changelog_agent.summarizer_service.app.agent.summarizer_agent import summarize_classified_commits
from src.changelog_agent.summarizer_service.app.prompts.summarizer_prompt import summarizer_prompt
from src.changelog_agent.summarizer_service.app.schemas.schema import SummarizerResults
from src.changelog_agent.summarizer_service.app.schemas.parser import summarizer_parser

__all__ = [
    'summarize_classified_commits',
    'summarizer_prompt',
    'summarizer_parser',
    'SummarizerResults',
]