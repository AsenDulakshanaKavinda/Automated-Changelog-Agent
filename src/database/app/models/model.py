from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text
from src.database.app.db.db import Base

class Table01(Base):
    __tablename__ = 'table01'

    id = Column(Integer, primary_key=True)









