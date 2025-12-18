from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# connection URL for database
URL_DATABASE = 'postgresql://postgres:postgres@localhost:5432/automated_changelog_agent'

engine = create_engine(URL_DATABASE)

# backend of the ORM ops.
engine = create_engine(URL_DATABASE)

#
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#
Base = declarative_base()