from typing import Optional
from pydantic import BaseModel

from datetime import date, datetime 


class CreatePerformanceDetails(BaseModel):
    comments: Optional[str]
    weight: Optional[str]
    final_score: Optional[str]
    performance_assessment: Optional[str]
    appraisal_form_id: Optional[int]
    overall_performance_id: Optional[int]
    

    class Config():
        orm_mode = True



class UpdatePerformanceDetails(BaseModel):
    id:Optional[int]
    comments: Optional[str]
    weight: Optional[str]
    final_score: Optional[str]
    performance_assessment: Optional[str]
    appraisal_form_id: Optional[int]
    overall_performance_id: Optional[int]




    class Config():
        orm_model = True 
    