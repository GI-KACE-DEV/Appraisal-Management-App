## db/session.py

## importing libraries
from email.generator import Generator
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import settings

SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

## lets create a dependency to guide our db connection
def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db 
    finally:
        db.close()