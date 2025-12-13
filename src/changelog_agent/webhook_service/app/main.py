

from fastapi import FastAPI
from app.api.github_webhook import router as github_router

# FastAPI app instance
app = FastAPI(title='Webhook Service')

# router inclusion
app.include_router(
    github_router,
    prefix='/webhook/github',
    tags=['Github Webhooks']
)

