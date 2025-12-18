
from src.database.app.db.db import get_db, engine
from src.database.app.models.webhook_table import WebhookTable
from src.database.app.schemas.schema import WebhookTableSchema
from sqlalchemy.orm import Session

from fastapi import APIRouter, Depends, HTTPException

from src.changelog_agent.utils.logger_config import log
from src.changelog_agent.utils.exception_config import ProjectException


router = APIRouter()

@router.post("/start")
def create_webhook(webhook: WebhookTableSchema, db: Session = Depends(get_db)):
    
    """ insert data to the tables """
    try:
        db_obj = WebhookTable(**webhook.model_dump())
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        log.info('webhook data store to the db tables.')
        return {'status': 'stored', "webhook_id": db_obj.webhook_id}
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

