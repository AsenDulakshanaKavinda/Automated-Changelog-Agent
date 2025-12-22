from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = 'postgresql+asyncpg://postgres:1234@localhost:5432/test-db-002'

settings = Settings()