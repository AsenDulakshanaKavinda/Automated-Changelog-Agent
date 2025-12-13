

def handle_pull_req(payload):
    pass

def handle_push(payload):
    repo = payload.get('repository', {}).get('name')
    author = payload.get('pusher', {}).get('name')

def handle_pull(payload):
    pass

def handle_pull(payload):
    pass



















