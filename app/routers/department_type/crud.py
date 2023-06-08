from utils import raise_exc, decode_jwt, schema_to_model, create_jwt
from  fastapi import HTTPException, Depends
from exceptions import BlacklistedToken
from sqlalchemy.orm import Session
from dependencies import get_db
from . import models, schemas
from config import settings
from cls import CRUD

async def create_department_type(depType:schemas.CreateDepType, db: Session):
    deptype = models.DepartmentType(title=depType.title)

    db.add(deptype)
    db.commit()
    db.refresh(deptype)
    return deptype 

