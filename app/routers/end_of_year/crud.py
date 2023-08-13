from fastapi.exceptions import HTTPException
from fastapi import status
from sqlalchemy.orm import Session
from routers.end_of_year.schemas import CreateEndofYearReview,UpdateEndofYearReview
from routers.end_of_year.models import EndofYearReview
from routers.appraisal_form.models import Appraisalview







async def create_new_end_of_year_review(end_of_year_review:CreateEndofYearReview, db:Session):
    end_of_year_review_object = EndofYearReview(**end_of_year_review.dict())
    
    db.add(end_of_year_review_object)
    db.flush()
    db.commit()
    db.refresh(end_of_year_review_object)
    return end_of_year_review_object









async def get_all_end_of_year_review(db:Session):
    data = db.query(EndofYearReview).all()
    return data





async def staff_end_of_year_review_form(appraisal_form_id: str, db:Session):
    data = db.query(EndofYearReview).filter(
        EndofYearReview.appraisal_form_id == Appraisalview.appraisal_form_id,
        EndofYearReview.appraisal_form_id == appraisal_form_id
        ).all()
    
    if not data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"End of Year Review form with the id {appraisal_form_id} is not found")
    return data











async def update_End_of_Year_Review(updateEndofYearReview: UpdateEndofYearReview, db:Session):
    end_of_year_review_id = updateEndofYearReview.id
    is_end_of_year_review_id_update = db.query(EndofYearReview).filter(EndofYearReview.id == end_of_year_review_id).update({
        EndofYearReview.appraisers_comment_on_workplan : updateEndofYearReview.appraisers_comment_on_workplan,
        EndofYearReview.training_development_comments : updateEndofYearReview.training_development_comments,
        EndofYearReview.appraisees_comments_and_plan : updateEndofYearReview.appraisees_comments_and_plan,
        EndofYearReview.head_of_divisions_comments : updateEndofYearReview.head_of_divisions_comments,
        EndofYearReview.average_per_rating : updateEndofYearReview.average_per_rating,
        EndofYearReview.average_total : updateEndofYearReview.average_total,
        EndofYearReview.average_per_rating_id : updateEndofYearReview.average_per_rating_id,
        EndofYearReview.approval_status : updateEndofYearReview.approval_status
        }, synchronize_session=False)
    db.flush()
    db.commit()
    if not is_end_of_year_review_id_update:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail="End of Year Review with the id (" + str(end_of_year_review_id) + ") is not found")

    data = db.query(EndofYearReview).filter(EndofYearReview.id == end_of_year_review_id).one()
    return data










# async def deleteEndofYearReview(id: str, db:Session):
#     db_data = db.query(EndofYearReview).filter(EndofYearReview.id == id).update({
#             EndofYearReview.status: 0
#             }, synchronize_session=False)
#     db.flush()
#     db.commit()
#     if not db_data:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#             detail=f"End of Year Review with the id {id} is not found")

#     data = db.query(EndofYearReview).filter(EndofYearReview.id == id).one()
#     return data

