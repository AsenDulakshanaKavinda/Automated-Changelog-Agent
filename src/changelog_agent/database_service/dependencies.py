from src.changelog_agent.database_service.database import SessionLocal

async def get_db():
    async with SessionLocal() as session:
        yield session

