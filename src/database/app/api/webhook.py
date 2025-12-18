
from src.database.app.db.db import get_db, engine
from src.database.app.models.webhook import WebhookTable
from src.database.app.schemas.schema import WebhookTableSchema
from sqlalchemy.orm import Session

from fastapi import APIRouter, Depends, HTTPException

from src.changelog_agent.utils.logger_config import log
from src.changelog_agent.utils.exception_config import ProjectException


router = APIRouter()

@router.post("/webhooks")
def create_webhook(webhook: WebhookTableSchema, db: Session = Depends(get_db)):
    db_obj = WebhookTable(**webhook.model_dump())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    log.info('creating table - webhook ')
    return {'status': 'stored', "webhook_id": db_obj.webhook_id}

@router.get("/webhooks")
def create_webhook_event(
        payload: WebhookTableSchema,
        db: Session = Depends(get_db),
):
    try:
        record = WebhookTable(
            webhook_id=payload.webhook_id,
            webhook_event=payload.webhook_event,
            repo_name=payload.repo_name,
            branch=payload.repo_branch,
            author=payload.author,
            timestamp=payload.timestamp,
            payload=payload.payload
        )
        log.info(f"webhook event data stored in db: {payload.webhook_event}")
        db.add(record)
        db.commit()
        db.refresh(record)



        return {'webhook_id': record.webhook_id, 'states': 'stored'}

    except Exception as e:
        db.rollback()
        ProjectException(
            e,
            context={
                'operation': 'create_webhook_event',
                'message': 'Webhook event creation failed',
            }
        )
        raise HTTPException(status_code=500, detail=str(e))









