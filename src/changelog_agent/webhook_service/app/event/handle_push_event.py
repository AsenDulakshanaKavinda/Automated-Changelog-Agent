from datetime import datetime

def handle_push_event(payload: dict) -> dict:
    commits = []

    for commit in payload.get("commits", []):
        commits.append({
            'sha': commit['id'],
            'message': commit['message'],
            'author': commit['author']['name'],
            'timestamp': commit['timestamp'],
            'files_changed': (
                commit.get('added', []) +
                commit.get('modified', []) +
                commit.get('removed', [])
            )
        })

    return {
        'event_type': 'push',
        'repo_name': payload['repository']['full_name'],
        'branch': payload['ref'].replace('refs/heads/', ''),
        'commits': commits,
        'pull_request': None,
        'metadata': {
            'source': 'github',
            'received_at': datetime.now().isoformat()
        }
    
    }










