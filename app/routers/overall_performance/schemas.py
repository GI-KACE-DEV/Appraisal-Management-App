from typing import Optional
from pydantic import BaseModel

from datetime import date, datetime 


class CreateOverallPerformance(BaseModel):
    description: Optional[str]
    performance: Optional[str]
    




    class Config():
        orm_mode = True



class UpdateOverallPerformance(BaseModel):
    id:Optional[int]
    description: Optional[str]
    performance: Optional[str]




    class Config():
        orm_model = True 
    