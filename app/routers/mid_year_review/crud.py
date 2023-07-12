from fastapi.exceptions import HTTPException
from fastapi import status
from sqlalchemy.orm import Session
from routers.mid_year_review.schemas import CreateMidYearReview,UpdateMidYearReview
from routers.mid_year_review.models import MidYearReview







async def create_new_mid_year_review(mid_year_review:CreateMidYearReview, db:Session):
    mid_year_review_object = MidYearReview(**mid_year_review.dict())
    
    db.add(mid_year_review_object)
    db.flush()
    db.commit()
    db.refresh(mid_year_review_object)
    return mid_year_review_object









async def get_all_mid_year_review(db:Session):
    data = db.query(MidYearReview).all()
    return data



async def get_mid_year_review_By_ID(id: int, db:Session):
    data = db.query(MidYearReview).filter(MidYearReview.id == id).all()
    
    if not data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Mid of Year Review with the id {id} is not found")
    return data








# async def update_Appraisal_Form(updateAppraisalForm: UpdateAppraisalForm, db:Session):
#     mid_year_review_id = updateAppraisalForm.mid_year_review_id
#     is_mid_year_review_id_update = db.query(AppraisalForm).filter(AppraisalForm.mid_year_review_id == mid_year_review_id).update({
#         AppraisalForm.department : updateAppraisalForm.department,
#         AppraisalForm.grade : updateAppraisalForm.grade,
#         AppraisalForm.positions : updateAppraisalForm.positions,
#         AppraisalForm.appraisal_date : updateAppraisalForm.appraisal_date,
#         }, synchronize_session=False)
#     db.flush()
#     db.commit()
#     if not is_mid_year_review_id_update:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#             detail=f"AppraisalForm with the id (" + str(mid_year_review_id) + ") is not found")

#     data = db.query(AppraisalForm).filter(AppraisalForm.mid_year_review_id == mid_year_review_id).one()
    return data










async def deleteAppraisalForm(id: int, db:Session):
    db_data = db.query(AppraisalForm).filter(AppraisalForm.id == id).update({
            AppraisalForm.status: 0
            }, synchronize_session=False)
    db.flush()
    db.commit()
    if not db_data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail=f"AppraisalForm with the id {id} is not found")

    data = db.query(AppraisalForm).filter(AppraisalForm.id == id).one()
    return data

