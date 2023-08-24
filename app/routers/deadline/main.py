from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from . import schemas, models, crud
from  dependencies import get_db




# APIRouter creates path operations for deadline module
deadline_router = APIRouter()


@deadline_router.post("/create")
async def create_new_deadline(deadline:schemas.CreateDeadline, db:Session = Depends(get_db)):

    return await crud.create_deadline(deadline=deadline, db=db)











@deadline_router.get("/all")
async def get_all_deadline(db:Session = Depends(get_db)):
    return await crud.get_deadline(db)










@deadline_router.get("/get/{supervisor_id}")
async def get_deadline_by_supervisor_id(supervisor_id: int, db:Session = Depends(get_db)):

    return await crud.get_deadline_by_supervisor_id(supervisor_id, db)









@deadline_router.get("/id/{id}")
async def get_deadline_by_id(id: int, db:Session = Depends(get_db)):

    return await crud.get_deadline_by_id(id, db)










@deadline_router.put("/update")
async def update_departmental_deadline(update: schemas.UpdateDeadline, db:Session = Depends(get_db)):
    
    return await crud.update_department_deadline(update, db)