from fastapi import APIRouter, Depends 
from dependencies import get_db
from sqlalchemy.orm import Session 
from . import crud, schemas
from dependencies import * 


## lets create an instance of APIRouter
deptype_router = APIRouter()

@deptype_router.post("/create/", response_model=schemas.ShowDepType)
async def create_new_deptype(deptype: schemas.CreateDepType, db:Session = Depends(get_db)):
    deptype = crud.create_department_type(deptype=deptype, db=db)
    return deptype

