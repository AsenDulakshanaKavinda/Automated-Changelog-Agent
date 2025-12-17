
"""
- Orchestrator Service
    - acts as the central brain of the changelog agent system.
    - responsible for coordinating multiple AI agent such as
        classification, summerization and review agents based on incoming event.
"""

# ===============================
# Orchestrator Service Metadata
# ===============================
__version__="0.1.0"
__author__="Asen Dulakshana"
__email__=""
__description__=(
    "Central orchestrator service for `Changelog Agent System`"
    "Receives structured inputs and coordinates multiple AI agents to generate automated changelogs."
)

# ===============================
# Orchestrator Service Metadata
# ===============================

from src.changelog_agent.orchestrator_service.app.api.orchestrator import router
from src.changelog_agent.orchestrator_service.app.schemas.orchestrator_input import (OrchestratorInput, )
from src.changelog_agent.orchestrator_service.app.background_tasks.tasks import run_orchestration

__all__ = [
    'router',
    'OrchestratorInput',
    'run_orchestration',
]


