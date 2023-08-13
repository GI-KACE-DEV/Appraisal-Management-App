from fastapi.exceptions import HTTPException
from fastapi import status
from sqlalchemy.orm import Session
from routers.performance_details.schemas import CreatePerformanceDetails,UpdatePerformanceDetails
from routers.performance_details.models import PerformanceDetails







async def create_new_performance_details(performance_details:CreatePerformanceDetails, db:Session):
    performance_details_object = PerformanceDetails(**performance_details.dict())
    
    db.add(performance_details_object)
    db.flush()
    db.commit()
    db.refresh(performance_details_object)
    return performance_details_object









async def get_all_performance_details(db:Session):
    data = db.query(PerformanceDetails).all()
    return data



async def get_performance_details_By_ID(id: str, db:Session):
    data = db.query(PerformanceDetails).filter(PerformanceDetails.id == id).all()
    
    if not data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Start Of Year with the id {id} is not found")
    return data








async def update_Performance_Details(updatePerformanceDetails: UpdatePerformanceDetails, db:Session):
    performance_details_id = updatePerformanceDetails.id
    is_performance_details_id_update = db.query(PerformanceDetails).filter(PerformanceDetails.id == performance_details_id).update({
        PerformanceDetails.comments : updatePerformanceDetails.comments,
        PerformanceDetails.weight : updatePerformanceDetails.weight,
        PerformanceDetails.final_score : updatePerformanceDetails.final_score,
        PerformanceDetails.performance_assessment : updatePerformanceDetails.performance_assessment
        }, synchronize_session=False)
    db.flush()
    db.commit()
    if not is_performance_details_id_update:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail="Performance Details with the id (" + str(performance_details_id) + ") is not found")

    data = db.query(PerformanceDetails).filter(PerformanceDetails.id == performance_details_id).one()
    return data










# async def deletePerformanceDetails(id: str, db:Session):
#     db_data = db.query(PerformanceDetails).filter(PerformanceDetails.id == id).update({
#             PerformanceDetails.status: 0
#             }, synchronize_session=False)
#     db.flush()
#     db.commit()
#     if not db_data:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#             detail=f"End of Year Review with the id {id} is not found")

#     data = db.query(PerformanceDetails).filter(PerformanceDetails.id == id).one()
#     return data

