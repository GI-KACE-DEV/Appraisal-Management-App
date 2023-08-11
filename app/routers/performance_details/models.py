from sqlalchemy import Column,Integer, String,Boolean, ForeignKey,Date,TIMESTAMP,text,TEXT
from sqlalchemy.orm import relationship
import datetime

from database import Base


class PerformanceDetails(Base):
    '''Performance Details Model'''
    
    __tablename__ = "performance_details"

    id = Column(Integer,primary_key=True,index=True)
    comments = Column(TEXT, nullable=True)
    approved_date = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    weight = Column(TEXT, nullable=True)
    final_score = Column(TEXT, nullable=True)
    appraisal_form_id = Column(Integer, ForeignKey("appraisal_forms.id"))
    overall_performance_id = Column(Integer, ForeignKey("overall_performance.id"))
    performance_assessment = Column(TEXT, nullable=True)
    status = Column(Boolean, default=True, nullable=True)
    submit = Column(Boolean, default=False, nullable=True)
    created_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
