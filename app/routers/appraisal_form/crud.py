from fastapi.exceptions import HTTPException
from fastapi import status
from sqlalchemy.orm import Session
from routers.appraisal_form.schemas import CreateAppraisalForm,UpdateAppraisalForm
from routers.users.account.models import User
from routers.appraisal_form.models import AppraisalForm



async def create_new_appraisal_form(appForm:CreateAppraisalForm, db:Session, staff_id):
    appform_object = AppraisalForm(**appForm.dict(), staff_id=staff_id)
    
    db.add(appform_object)
    db.commit()
    db.refresh(appform_object)
    return appform_object





# async def get_all_appraisal_form(db:Session):
#     data = db.query(AppraisalForm).all()
#     return data






# async def get_appraisal_formBy_ID(id: int, db:Session):
#     data = db.query(AppraisalForm).filter(AppraisalForm.appraisal_form_id == id).all()
    
#     if not data:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"AppraisalForm with the id {id} is not found")
#     return data







async def updateAppraisalForm(updateAppraisalForm: UpdateAppraisalForm, db:Session):
    appraisal_form_id = updateAppraisalForm.appraisal_form_id
    is_appraisal_form_id_update = db.query(AppraisalForm).filter(AppraisalForm.appraisal_form_id == appraisal_form_id).update({
        AppraisalForm.department : updateAppraisalForm.department,
        AppraisalForm.grade : updateAppraisalForm.grade,
        AppraisalForm.positions : updateAppraisalForm.positions,
        AppraisalForm.appraisal_date : updateAppraisalForm.appraisal_date,
        }, synchronize_session=False)
    db.flush()
    db.commit()
    if not is_appraisal_form_id_update:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail=f"AppraisalForm with the id (" + str(appraisal_form_id) + ") is not found")

    data = db.query(AppraisalForm).filter(AppraisalForm.appraisal_form_id == appraisal_form_id).one()
    return data










async def deleteAppraisalForm(id: int, db:Session):
    db_data = db.query(AppraisalForm).filter(AppraisalForm.appraisal_form_id == id).update({
            AppraisalForm.status: 0
            }, synchronize_session=False)
    db.flush()
    db.commit()
    if not db_data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail=f"AppraisalForm with the id {id} is not found")

    data = db.query(AppraisalForm).filter(AppraisalForm.appraisal_form_id == id).one()
    return data

