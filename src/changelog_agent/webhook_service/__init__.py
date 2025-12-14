
"""
- WebhookService
    - acts as the entry point of the Changelog Agent System.
    - receives external webhook events (e.g., GitHub events).
    - validates, parses, and normalizes incoming events.
    - forwards structured data to the Orchestrator Service for further processing.
"""

# ===============================
# Orchestrator Service Metadata
# ===============================
__version__="0.1.0"
__author__="Asen Dulakshana"
__email__=""
__description__ = (
    "Webhook service for the Changelog Agent System. "
    "Receives external events, validates payloads, "
    "and forwards structured inputs to the Orchestrator Service."
)

# ===============================
# Webhook Service Metadata
# ===============================

from src.changelog_agent.webhook_service.app.api.github_webhook import github_webhook
from src.changelog_agent.webhook_service.app.core.security import verify_github_signature
from src.changelog_agent.webhook_service.app.event.handle_push_event import handle_push_event
from src.changelog_agent.webhook_service.app.schemas.orchestrator_input import OrchestratorInput
from src.changelog_agent.webhook_service.app.services.orchestrator_client import send_to_orchestrator

__all__ = [
    'github_webhook',
    'verify_github_signature',
    'handle_push_event',
    'OrchestratorInput',
    'send_to_orchestrator',
]