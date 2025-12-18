
import json
from datetime import datetime

from fastapi import APIRouter, Request, HTTPException
from pydantic import ValidationError

from src.changelog_agent.webhook_service.app.core.security import verify_github_signature
from src.changelog_agent.webhook_service.app.event.event_handler import event_handler
from src.changelog_agent.webhook_service.app.services.orchestrator_client import send_to_orchestrator
from src.changelog_agent.webhook_service.app.services.db_client import send_to_db
from src.changelog_agent.webhook_service.app.schemas.orchestrator_input import OrchestratorInput
from src.changelog_agent.webhook_service.app.schemas.db_input import WebhookTableSchema

from src.changelog_agent.utils.exception_config import ProjectException
from src.changelog_agent.utils.logger_config import log




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

def validate_signature(signature: str, raw_body: bytes, secret: str):
    """
    Validates GitHub webhook signature.

    - Raises HTTPException if invalid
    - Returns True if valid
    """

    if not signature:
        log.error("Missing X-Hub-Signature header")
        raise HTTPException(status_code=400, detail="Missing X-Hub-Signature header")
    
    try:
        log.info("GitHub signature validated successfully")
        return verify_github_signature(raw_body, secret, signature)
    except Exception as e:
        log.error("GitHub signature validation failed")
        raise HTTPException(status_code=403, detail="Invalid webhook signature")



    """ validate the signature """
    if not signature:
        log.error('No signature received to validate')
        raise HTTPException(status_code=400, detail='Missing X-Hub-Signature header')
    return verify_github_signature(raw_body, GITHUB_SECRET, signature)

    


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
        send_to_orchestrator = (valid_orchestrator_data.model_dump())
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
