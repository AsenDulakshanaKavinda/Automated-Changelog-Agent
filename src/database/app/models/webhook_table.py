from sqlalchemy import String, DateTime, JSON
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime

from src.database.app.db.base import Base

class WebhookTable(Base):
    __tablename__ = 'webhook'

    webhook_id: Mapped[str] = mapped_column(primary_key=True)
    webhook_event: Mapped[str] = mapped_column(String, nullable=False)
    repo_name: Mapped[str] = mapped_column(String, nullable=False)
    branch: Mapped[str | None] = mapped_column(String, nullable=True)
    author: Mapped[str | None] = mapped_column(String, nullable=True)
    # timestamp: Mapped[str | datetime| None] = mapped_column(DateTime, nullable=False, default=datetime.now)
    # payload: Mapped[dict] = mapped_column(JSON, nullable=False)









