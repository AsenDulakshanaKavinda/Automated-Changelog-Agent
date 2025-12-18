import json
from datetime import datetime

from fastapi import APIRouter, Request, HTTPException
from pydantic import ValidationError

from src.changelog_agent.webhook_service.app.api.github_helper import *

from src.changelog_agent.webhook_service.app.core.security import verify_github_signature
from src.changelog_agent.webhook_service.app.event.event_handler import event_handler
from src.changelog_agent.webhook_service.app.services.orchestrator_client import send_to_orchestrator
from src.changelog_agent.webhook_service.app.services.db_client import send_to_db
from src.changelog_agent.webhook_service.app.schemas.orchestrator_input import OrchestratorInput
from src.changelog_agent.webhook_service.app.schemas.db_input import WebhookTableSchema

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
    # FastAPI router and endpoint for handling incoming GitHub webhooks.

    # Args:
       request (Request): Request object.
    """

    # read raw request body
    raw_body = await request.body()
    
    # extract required headers
    webhook_id = request.headers['X-GitHub-Hook-ID']
    delivery_id = request.headers.get('X-GitHub-Delivery')
    webhook_event = request.headers.get('X-GitHub-Event')
    signature = request.headers.get('X-Hub-Signature')
    
    if not webhook_event:
        raise HTTPException(status_code=400, detail="Missing X-GitHub-Event header")

    if not delivery_id:
        log.warning("Missing X-GitHub-Delivery header")

    # validate signature
    if not validate_signature(signature, raw_body, GITHUB_SECRET):
        raise HTTPException(status_code=400, detail='failed to verify the signature')

    # create the payload
    payload = extract_payload(raw_body)
    log.info('Payload created')

    repo_name = payload['repository']['name']
    branch = payload.get('ref')
    author = payload.get("sender", {}).get("login")

    # build orchestrator input
    try:
        orchestrator_input_dict = event_handler(
            event=webhook_event,
            payload=payload
        )
        orchestrator_input = OrchestratorInput(**orchestrator_input_dict)
    except ValidationError as e:
        log.error("Invalid orchestrator input")
        raise HTTPException(status_code=422, detail=str(e))

    # send to orchestrator
    try:
        send_to_orchestrator(orchestrator_input.model_dump())
        log.info("Event sent to orchestrator")
    except Exception as e:
        ProjectException(
            e,
            context={
                "operation": "send_to_orchestrator",
                "delivery_id": delivery_id,
            }
        )
        raise HTTPException(status_code=502, detail="Failed to dispatch event")

    # build database input
    try:
        db_input_dict = {
            'webhook_id' : webhook_id,
            'webhook_event' : webhook_event,
            'repo_name' : repo_name,
            'branch' : branch,
            'author' : author,
            # 'timestamp' : str(datetime.now),
            # 'payload' : payload,
        }
        log.info("\n\n")
        for key, value in db_input_dict.items():
            log.info(f"Key: {key}, Value: {value}, type: {type(value)}")
        log.info("\n")
        db_input = WebhookTableSchema(**db_input_dict)
    except ValidationError as e:
        log.error("Invalid db input")
        raise HTTPException(status_code=422, detail=str(e))

    # send to db
    try:
        send_to_db(db_input.model_dump())
        log.info('Event sent to database')
    except Exception as e:
        ProjectException(
            e,
            context={
                "operation": "send_to_orchestrator",
                "delivery_id": delivery_id,
            }
        )
        raise HTTPException(status_code=502, detail="Failed to store event in db")   

    return {'status': 'accepted'}
