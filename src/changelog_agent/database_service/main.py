
from fastapi import FastAPI, Request
from contextlib import asynccontextmanager

from src.changelog_agent.database_service.database import engine, Base
from src.changelog_agent.database_service.models import webhook, classifier
from src.changelog_agent.database_service.routers.webhook import router

from src.changelog_agent.utils.logger_config import log

@asynccontextmanager
async def lifespan(app: FastAPI):

    app.state.engine = engine

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    log.info("Application startup complete. Database tables ensured.")
    yield

    await engine.dispose()
    log.info("Application shutdown complete.")

app = FastAPI(
    title="My FastAPI Project",
    description="A clean, scalable FastAPI application with database support",
    version="1.0.0",
    lifespan=lifespan,
    docs_url="/docs",      # Swagger UI
    redoc_url="/redoc",    # Alternative docs
)

""" @app.exception_handler(Exception)
async def all_exception_handler(request: Request, exc: Exception):
    # full traceback to your logger
    log.error("Unhandled exception at %s %s\n%s", request.method, request.url, traceback.format_exc())
    return JSONResponse({"detail": "Internal Server Error"}, status_code=500)
 """

@app.get("/")
async def root():
    return {"message": "Welcome to Automated Chanalog Agent DB Service! Visit /docs for the API documentation."}


app.include_router(
    router,
    prefix='/webhook',
    tags=['webhook']
)


