from fastapi import Request, HTTPException, Depends

from exceptions import BlacklistedToken
from database import SessionLocal
from email.generator import Generator


def get_db() -> Generator:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

