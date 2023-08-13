from fastapi.exceptions import HTTPException
from fastapi import status
from sqlalchemy.orm import Session
from routers.overall_performance.schemas import CreateOverallPerformance,UpdateOverallPerformance
from routers.overall_performance.models import OverallPerformance







async def create_new_overall_performance(overall_performance:CreateOverallPerformance, db:Session):
    overall_performance_object = OverallPerformance(**overall_performance.dict())
    
    db.add(overall_performance_object)
    db.flush()
    db.commit()
    db.refresh(overall_performance_object)
    return overall_performance_object









async def get_all_overall_performance(db:Session):
    data = db.query(OverallPerformance).all()
    return data



async def get_overall_performance_By_ID(id: str, db:Session):
    data = db.query(OverallPerformance).filter(OverallPerformance.id == id).all()
    
    if not data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Overall Performance with the id {id} is not found")
    return data








async def update_Overall_Performance(updateOverallPerformance: UpdateOverallPerformance, db:Session):
    overall_performance_id = updateOverallPerformance.id
    is_overall_performance_id_update = db.query(OverallPerformance).filter(OverallPerformance.id == overall_performance_id).update({
        OverallPerformance.description : updateOverallPerformance.description,
        OverallPerformance.performance : updateOverallPerformance.performance
        }, synchronize_session=False)
    db.flush()
    db.commit()
    if not is_overall_performance_id_update:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail="Overall Performance with the id (" + str(overall_performance_id) + ") is not found")

    data = db.query(OverallPerformance).filter(OverallPerformance.id == overall_performance_id).one()
    return data










# async def deleteOverallPerformance(id: str, db:Session):
#     db_data = db.query(OverallPerformance).filter(OverallPerformance.id == id).update({
#             OverallPerformance.status: 0
#             }, synchronize_session=False)
#     db.flush()
#     db.commit()
#     if not db_data:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#             detail=f"OverallPerformance with the id {id} is not found")

#     data = db.query(OverallPerformance).filter(OverallPerformance.id == id).one()
#     return data

