from typing import Any

from src.changelog_agent.utils.exception_config import ProjectException
from src.changelog_agent.utils.logger_config import log

def handle_push_event(payload: dict):
    """
    handle push event

    Args:
        payload:

    Returns:
        Orchestrator response

    """
    commits = []
    try:
        for commit in payload.get("commits", []):
            commits.append({
                'sha': commit['id'],
                'message': commit['message'],
                'author': commit['author']['name'],
                'timestamp': commit['timestamp'],
                'file_changed': (
                    commit.get('added', []) +
                    commit.get('modified', []) +
                    commit.get('removed', [])
                )
            })
            log.info(f'handling commit {commit["id"]}, message {commit["message"]}')

        return {
            'event_type': 'push',
            'repo_name': payload['repository']['full_name'],
            'branch': payload['ref'].replace('refs/heads/', ''),
            'commits': commits,
            'pull_request': None,
            'metadata': {
                "before": payload.get("before"),
                "after": payload.get("after"),
                "sender": payload.get("sender"),
            }

        }
    except Exception as e:
        ProjectException(
            e,
            context={
                'operation': 'push handler',
                'message': 'push handler error',
            }
        )











