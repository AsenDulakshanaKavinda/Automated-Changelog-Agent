
from fastapi import APIRouter, Request, Header, HTTPException
from app.core.security import verify_github_signature
from app.services.orchestrator_client import send_to_orchestrator
from app.event.handle_push_event import handle_push_event
from datetime import datetime
import os

# API router instance
router = APIRouter()

# GitHub webhook secret from .env
GITHUB_SECRET = os.getenv('GITHUB_WEBHOOK_SECRET', 'supersecret')


@router.post('/')
async def github_webhook(
    
    request: Request,
    x_github_event: str = Header(None),
    x_hub_signature_256: str = Header(None)
):
    """ FastAPI router and endpoint for handling incoming GitHub webhooks """
    
    # read raw request body
    raw_body = await request.body()

    # verify signature
    if not verify_github_signature(
        raw_body, x_hub_signature_256, GITHUB_SECRET
    ):
        raise HTTPException(status_code=401, detail='Invalid signature.')
    
    # parse the body as JSON
    payload = await request.json()

    # event -> push
    if x_github_event == 'push':
        orchestrator_input = handle_push_event(payload=payload)
    # * -- other event also go here --
    
    else:
        # if no x_github_event
        return {'status': 'ignored', 'event': x_github_event}
    
    # send to orchestrator
    # send_to_orchestrator(orchestrator_input)

    return {'status': 'accepted'}



    


























