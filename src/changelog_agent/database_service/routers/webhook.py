
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends, Request, HTTPException
from src.changelog_agent.database_service.schemas.webhook import WebhookCreate, WebhookResponse
from src.changelog_agent.database_service.dependencies import get_db
from src.changelog_agent.database_service.services.webhook_service import create_webhook
from src.changelog_agent.webhook_service.app.schemas.webhook_input import WebhookInput

from src.changelog_agent.utils.exception_config import ProjectException
from src.changelog_agent.utils.logger_config import log



router = APIRouter()

@router.post('/', response_model=WebhookResponse)
async def create_webhook_endpoint(webhook: WebhookCreate, db: AsyncSession=Depends(get_db)):
    db_webhook = await create_webhook(db=db, webhook_in=webhook)
    return db_webhook

@router.post('/start', response_model=None)
async def github_webhook(request: Request, db: AsyncSession=Depends(get_db)):
    payload = await request.json()

    try:
        webhook_data = WebhookCreate(
            webhook_id=payload['webhook_id'],
            webhook_event=payload['webhook_event'],
            repo_name=payload['repo_name'],
            author=payload['author'],
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

    db_webhook = await create_webhook(db=db, webhook_in=webhook_data)
    log.info("Webhook saved successfully")

    return db_webhook

