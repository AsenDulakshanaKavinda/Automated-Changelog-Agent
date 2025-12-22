from sqlalchemy import Column, ForeignKey, Integer, Boolean, String, Float, ARRAY
from src.changelog_agent.database_service.database import Base

from sqlalchemy.orm import relationship

class Classifier(Base):
    __tablename__ = 'classifier'

    id = Column(Integer, primary_key=True, index=True)
    # Proper foreign key to the primary key of webhook_events
    webhook_id_ref = Column(Integer, ForeignKey('webhook_events.id', ondelete="CASCADE"), nullable=False)
    comment_sha = Column(String)
    type = Column(String)
    message = Column(String)
    breaking_change = Column(Boolean, default=False)
    confidence = Column(Float)
    files_changed = Column(ARRAY(String))

    webhook = relationship("Webhook", back_populates="classifiers")














