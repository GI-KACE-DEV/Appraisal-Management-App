from typing import Optional
from pydantic import BaseModel

from datetime import date, datetime 


class CreatePerformanceDetails(BaseModel):
    comments: Optional[str]
    weight: Optional[str]
    final_score: Optional[str]
    performance_assessment: Optional[str]
    appraisal_form_id: Optional[str]
    overall_performance_id: Optional[str]
    

    class Config():
        orm_mode = True



class UpdatePerformanceDetails(BaseModel):
    id:Optional[str]
    comments: Optional[str]
    weight: Optional[str]
    final_score: Optional[str]
    performance_assessment: Optional[str]
    appraisal_form_id: Optional[str]
    overall_performance_id: Optional[str]




    class Config():
        orm_model = True 
    