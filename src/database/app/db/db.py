from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# connection URL for database
DATABASE_URL='postgresql+psycopg2://postgres:1234@localhost:5432/test_aca'


engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# get the db connection
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



