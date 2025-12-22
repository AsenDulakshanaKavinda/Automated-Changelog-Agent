

from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from src.changelog_agent.database_service.schemas.webhook import WebhookCreate
from src.changelog_agent.database_service.models.webhook import Webhook



async def create_webhook(db: AsyncSession, webhook_in: WebhookCreate) -> Webhook:
    db_webhook = Webhook(
        webhook_id = webhook_in.webhook_id,
        webhook_event = webhook_in.webhook_event,
        repo_name = webhook_in.repo_name,
        author = webhook_in.author
    ) 

    db.add(db_webhook)
    await db.commit()
    await db.refresh(db_webhook)
    return db_webhook













