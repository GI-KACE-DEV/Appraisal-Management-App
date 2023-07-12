from typing import Optional
from pydantic import BaseModel

from datetime import date, datetime 


class CreateEndofYearReview(BaseModel):
    appraisers_comment_on_workplan: Optional[str]
    training_development_comments: Optional[str]
    appraisees_comments_and_plan: Optional[str]
    head_of_divisions_comments: Optional[str]
    average_per_rating: Optional[str]
    average_total: Optional[str]
    average_per_rating_id: Optional[str]
    appraisal_form_id: Optional[int]
    performance_details_id: Optional[int]
    

    class Config():
        orm_mode = True



class UpdateEndofYearReview(BaseModel):
    id:Optional[int]
    appraisers_comment_on_workplan: Optional[str]
    training_development_comments: Optional[str]
    appraisees_comments_and_plan: Optional[str]
    head_of_divisions_comments: Optional[str]
    average_per_rating: Optional[str]
    average_total: Optional[str]
    average_per_rating_id: Optional[str]
    appraisal_form_id: Optional[int]
    performance_details_id: Optional[int]




    class Config():
        orm_model = True 
    