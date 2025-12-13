
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

def handle_push(payload):
    repo = payload['repository']['name']
    author = payload['pusher']['name']

    commits = payload.get('commits', [])
    for commit in commits: 
        print('commit', commit['message'])

    print(f'repo: {repo}' )
    print(f'author: {author}')
    


def handle_pull_request(payload):
    action = payload["action"]

    pr = payload["pull_request"]
    pr_title = pr["title"]
    pr_author = pr["user"]["login"]
    pr_url = pr["html_url"]

    print("PR Action:", action)
    print("Title:", pr_title)
    print("Author:", pr_author)
    print("URL:", pr_url)


EVENT_HANDLERS = {
    'push': handle_push,
    'pull_request': handle_pull_request
}


@app.post('/')
async def webhook(request: Request):
    payload = await request.json()
    event_type = request.headers.get("X-GitHub-Event")

    handler = EVENT_HANDLERS.get(event_type)

    if handler:
        handler(payload)
    else:
        print(f'No handler for {event_type}')

    return {"status": "ok"}