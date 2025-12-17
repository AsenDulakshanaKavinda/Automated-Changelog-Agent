
"""
- Classification Service
    - acts as the commit classification agent of the Changelog Agent System.
    - receives commits from the webhook service.
    - then classify the commit to (feature, bug ...)
    - forwards structured classification data to the Orchestrator Service for further processing (summarize the commit).
"""

# ===============================
# Classification Service Metadata
# ===============================
__version__="0.1.0"
__author__="Asen Dulakshana"
__email__=""
__description__ = (
    "Classification service for the Changelog Agent System. "
    "Receives commits and metadata from the webhook,"
    "and forwards structured classification inputs to the Orchestrator Service."
)

# ===============================
# Classification Service Metadata
# ===============================

from src.changelog_agent.classifier_service.app.agent.classification_agent import classify_commits
from src.changelog_agent.classifier_service.app.prompts.classification_prompt import classifier_prompt
from src.changelog_agent.classifier_service.app.schemas.schema import ClassificationResult
from src.changelog_agent.classifier_service.app.schemas.parser import classification_parser

__all__ = [
    'classify_commits',
    'classifier_prompt',
    'ClassificationResult',
    'classification_parser',
]