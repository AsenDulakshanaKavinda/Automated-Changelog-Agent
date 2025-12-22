from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from src.changelog_agent.database_service.database import Base


class Webhook(Base):
    __tablename__ = 'webhook_events'

    id = Column(Integer, primary_key=True)
    webhook_id = Column(String, unique=True)
    webhook_event = Column(String)
    repo_name = Column(String)
    author = Column(String)

    classifiers = relationship(
        "Classifier",
        back_populates="webhook",
        cascade="all, delete-orphan",  # Optional: auto-delete classifiers if webhook deleted
        passive_deletes=True
    )







