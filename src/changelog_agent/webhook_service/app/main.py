
from fastapi import FastAPI
from .api.github_webhook import router as github_router


# FastAPI app instance
app = FastAPI(title='Webhook Service')

# router inclusion
app.include_router(
    github_router,
    prefix='/webhooks/github',
    tags=['Github Webhooks']
)

