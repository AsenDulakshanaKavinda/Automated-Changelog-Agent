
"""
- Utils Package
    - provides utility functions and classes for the Changelog Agent System.
    - includes custom exceptions for project-specific error handling.
    - offers logging utilities for general logging, auditing, and performance tracking.
"""

# ===============================
# Utils Package Metadata
# ===============================
__version__="0.1.0"
__author__="Asen Dulakshana"
__email__=""
__description__ = (
    "Utility package for the Changelog Agent System. "
    "Provides custom exceptions and logging configurations "
    "for error handling and monitoring throughout the system."
)

from src.changelog_agent.utils.exception_config import ProjectException
from src.changelog_agent.utils.logger_config import log, audit_log, performance_log

__all__ = [
    'ProjectException',
    'log',
    'audit_log',
    'performance_log',
]




