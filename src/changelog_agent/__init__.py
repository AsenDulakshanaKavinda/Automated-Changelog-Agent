"""
- Webhook Service
    - acts as the entry point for the Changelog Agent System.
    - receives webhook notifications from version control systems (e.g., GitHub, GitLab).
    - validates and processes incoming webhook payloads.
    - extracts commit data and forwards it to the Classification Service for categorization.
"""

# ===============================
# Webhook Service Metadata
# ===============================
__version__="0.1.0"
__author__="Asen Dulakshana"
__email__=""
__description__ = (
    "Webhook service for the Changelog Agent System. "
    "Handles incoming webhook events, processes commit information, "
    "and forwards data to the Orchestrator Service."
)