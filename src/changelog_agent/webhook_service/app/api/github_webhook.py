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



    return {'status': 'accepted'}





    """ log.info(f'webhook_id: {webhook_id}, type: {type(webhook_id)}')
    log.info(f'webhook_event: {webhook_event}, type: {type(webhook_event)}')
    log.info(f'signature: {signature}, type: {type(signature)}')
    log.info(f'repo_name: {repo_name}, type: {type(repo_name)}')
    log.info(f'branch: {branch}, type: {type(branch)}')
    log.info(f'author: {author}, type: {type(author)}')
    # log.info(f'author: {author}, type: {type(author)}')


    # if header missing
    if not webhook_event:
        log.warning(f'No event received from {request.url}')
        raise HTTPException(status_code=400, detail='Missing X-GitHub-Event header')

    # handle signature and verify signature
    if not signature:
        log.warning(f'No signature received from {request.url}')
        raise HTTPException(status_code=403, detail='Missing X-Hub-Signature header')
    verify_github_signature(raw_body, GITHUB_SECRET, signature)

    # if delivery missing
    if not delivery:
        log.warning(f'No delivery received from {webhook_event}')

    # parse the body as JSON
    try:
        payload = json.loads(raw_body.decode('utf-8'))
        log.info(f'Payload received from {webhook_event}')
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

    orchestrator_input = event_handler(webhook_event, payload)

    try:
        validated_orchester_input = OrchestratorInput(**orchestrator_input)
    except ValidationError as e:
        log.error(f'Validation error: {e}')
        raise HTTPException(status_code=402, detail=str(e))

    # send to orchestrator
    try:
        send_to_orchestrator(validated_orchester_input.model_dump())
        return {'status': 'accepted'}
    except Exception as e:
        ProjectException(
            e,
            context={
                'operation': 'github_webhook',
                'message': 'Failed to send to orchestrator',
            }
        )

    # - helper functions
    def extract_payload(raw_body: bytes):
        try:
            payload = json.loads(raw_body.decode('utf-8'))
            log.info('Payload extracted from the raw body')
            return payload
        except Exception as e:
            ProjectException(
                e, 
                context={
                    'operation': 'extract payload',
                    'message': f'error: {str(e)}'
                }
            )
            raise HTTPException(status_code=400, detail='Invalid JSON payload')

    def validate_signature(signature, raw_body, GITHUB_SECRET):
        
        if not signature:
            log.error('No signature received to validate')
            raise HTTPException(status_code=400, detail='Missing X-Hub-Signature header')
        verify_github_signature(raw_body, GITHUB_SECRET, signature)
        


    def handle_orchestrator_input(webhook_event, payload):

        # orchestrator input
        orchestrator_input = event_handler(event=webhook_event, payload=payload)

        # validate the orchestrator_input
        try:
            validated_orchester_input = OrchestratorInput(**orchestrator_input)
            return validated_orchester_input
            log.info('Orchestrator input valid.')
        except Exception as e:
            log.error(f'orchesterinput validatedation failed.')
            raise HTTPException(status_code=402, detail=str(e))

    def handle_orchestrator(valid_orchestrator_data):
        try:
            send_to_orchestrator = (validated_orchester_input.model_dump())
            # return {'status': 'accepted'}
        except Exception as e:
            ProjectException(
            e,
            context={
                'operation': 'github_webhook',
                'message': 'Failed to send to orchestrator',
            }
        )
            
    def create_and_validate_db_input():
        pass



































































    # sent to db ----
    db_input = {
        'webhook_id': webhook_id,
        'webhook_event': webhook_event,
        'repo_name': repo_name,
        'branch': branch,
        'author': author,
        'timestamp': datetime.now(),
        'payload': payload,
    }


    # validata data ---
    try:
        # validated_db_input = WebhookTableSchema(**db_input)
        log.info('db input is valid')
    except Exception as e:
        ProjectException(
            e,
            context={
                'operation': 'github_webhook',
                'message': 'Failed to validate db input',
            }
        )
    # send data ---
    try:
        # send_to_db(validated_db_input.model_dump())
        log.info('sending data to db service')
        return {'status': 'accepted'}
    except Exception as e:
        ProjectException(
            e,
            context={
                'operation': 'github_webhook',
                'message': 'Failed to send to DB',
            }
        )
























 """