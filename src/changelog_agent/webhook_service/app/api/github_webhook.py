import json

from fastapi import APIRouter, Request, HTTPException
from pydantic import ValidationError

from src.changelog_agent.webhook_service.app.core.security import verify_github_signature
from src.changelog_agent.webhook_service.app.event.event_handler import event_handler
from src.changelog_agent.webhook_service.app.services.orchestrator_client import send_to_orchestrator
from src.changelog_agent.webhook_service.app.schemas.orchestrator_input import OrchestratorInput

from src.changelog_agent.utils.exception_config import ProjectException
from src.changelog_agent.utils.logger_config import log

import os
from dotenv import load_dotenv

# read the .env
load_dotenv()

# API router instance
router = APIRouter()

# GitHub webhook secret from .env
GITHUB_SECRET = os.getenv('GITHUB_WEBHOOK_SECRET', 'supersecret')
log.info(f'GITHUB_SECRET Read: {len(GITHUB_SECRET)}')

@router.post('/')
async def github_webhook(request: Request):
    """
    FastAPI router and endpoint for handling incoming GitHub webhooks.

    Args:
        request (Request): Request object.
    """
    
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

    # handle signature and verify signature
    if not signature:
        log.warning(f'No signature received from {request.url}')
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
                'operation': 'github_webhook',
                'message': 'Failed to decode payload',
            },
            reraise=False
        )
        raise HTTPException(status_code=400, detail='Invalid JSON payload')

    orchestrator_input = event_handler(event, payload)

    try:
        validated_input = OrchestratorInput(**orchestrator_input)
    except ValidationError as e:
        log.error(f'Validation error: {e}')
        raise HTTPException(status_code=402, detail=str(e))

    # send to orchestrator
    try:
        send_to_orchestrator(validated_input.model_dump())
        return {'status': 'accepted'}
    except Exception as e:
        ProjectException(
            e,
            context={
                'operation': 'github_webhook',
                'message': 'Failed to send to orchestrator',
            }
        )


























