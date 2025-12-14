import json

from fastapi import APIRouter, Request, Header, HTTPException
from sqlalchemy import false

from src.changelog_agent.webhook_service.app.core.security import verify_github_signature
from src.changelog_agent.webhook_service.app.event.handle_pull_req_event import handle_pull_req_event
from src.changelog_agent.webhook_service.app.event.handle_push_event import handle_push_event
from src.changelog_agent.webhook_service.app.services.orchestrator_client import send_to_orchestrator


from src.changelog_agent.utils.exception_config import ProjectException
from src.changelog_agent.utils.logger_config import log

from datetime import datetime
import os
from dotenv import load_dotenv

# read the .env
load_dotenv()

# API router instance
router = APIRouter()

# GitHub webhook secret from .env
GITHUB_SECRET = os.getenv('GITHUB_WEBHOOK_SECRET', 'supersecret')
log.info(f'GITHUB_SECRET: {GITHUB_SECRET}')

EVENT_HANDLERS = {
    "push": handle_push_event,
    "pull_request": handle_pull_req_event,
}

@router.post('/')
async def github_webhook(request: Request):
    """ FastAPI router and endpoint for handling incoming GitHub webhooks """
    
    # read raw request body
    raw_body = await request.body()

    # extract required headers
    event = request.headers.get('X-GitHub-Event')
    signature = request.headers.get('X-Hub-Signature')
    delivery = request.headers.get('X-GitHub-Delivery')

    # if header missing
    if not event:
        log.warning(f'No event received from {request.url}')
        raise HTTPException(status_code=400, detail='Missing X-GitHub-Event header')

    #
    if not signature:
        raise HTTPException(status_code=403, detail='Missing X-Hub-Signature header')
    verify_github_signature(raw_body, GITHUB_SECRET,signature)

    # if delivery missing
    if not delivery:
        log.warning(f'No delivery received from {event}')

    # parse the body as JSON
    try:
        payload = json.loads(raw_body.decode('utf-8'))
        log.info(f'Payload received from {event}')
    except Exception as e:
        ProjectException(
            e,
            context={
                'operation': 'github_webhook'
            },
            reraise=False
        )
        raise HTTPException(status_code=400, detail='Invalid JSON payload')

    handler = EVENT_HANDLERS.get(event)
    if not handler:
        return {"status": "ignored", "event": event}

    orchestrator_input = handler(payload)
    
    # send to orchestrator
    send_to_orchestrator(orchestrator_input)

    return {'status': 'accepted'}



    


























