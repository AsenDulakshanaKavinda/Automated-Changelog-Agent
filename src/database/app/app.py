from fastapi import FastAPI
from contextlib import asynccontextmanager

from src.database.app.db.db import engine
from src.database.app.db.base import Base
from src.database.app.api.webhook import router as webhook_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup logic
    Base.metadata.create_all(bind=engine)
    yield
    # shutdown logic
    engine.dispose()


app = FastAPI(title="Database", lifespan=lifespan)

app.include_router(webhook_router)