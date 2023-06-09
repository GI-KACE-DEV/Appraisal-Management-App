from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from . import schemas, models, crud
from  dependencies import get_db




# APIRouter creates path operations for AppraisalForm module
appraisalForm_router = APIRouter()


@appraisalForm_router.post("/create", response_description="AppraisalForm data added into the database")
async def create_new_appraisal_form(appraisalForm:schemas.CreateAppraisalForm, db:Session = Depends(get_db)):
    
    return await crud.create_new_appraisal_form(appraisalForm, db)







@appraisalForm_router.get("/getAppraisalForm")
async def get_all_appraisal_form(db:Session = Depends(get_db)):

    return await crud.get_all_appraisal_form(db)






@appraisalForm_router.get("/getAppraisalFormById/{id}")
async def getAppraisalFormById(id: int, db:Session = Depends(get_db)):
    
    return await crud.get_appraisal_formBy_ID(id, db)







@appraisalForm_router.put("/updateAppraisalForm")
async def updateAppraisalForm(updateStaff: schemas.UpdateAppraisalForm, db:Session = Depends(get_db)):
    
    return await crud.updateAppraisalForm(updateStaff, db)








@appraisalForm_router.delete("/deleteAppraisalForm/{id}")
async def deleteAppraisalForm(id: int, db:Session = Depends(get_db)):
    
    return await crud.deleteAppraisalForm(id, db)
