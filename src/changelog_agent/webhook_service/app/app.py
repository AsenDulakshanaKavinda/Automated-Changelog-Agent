
from fastapi import FastAPI
from src.changelog_agent.webhook_service.app.api.github_webhook import router

# FastAPI app instance
app = FastAPI(title='Webhook Service')

# router inclusion
app.include_router(
    router
)

