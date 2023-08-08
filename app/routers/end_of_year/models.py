from sqlalchemy import Column,Integer, String,Boolean, ForeignKey,Date,TIMESTAMP,text,TEXT
from sqlalchemy.orm import relationship
import datetime

from database import Base


class EndofYearReview(Base):
    '''End of Year Review Model'''
    
    __tablename__ = "end_of_year_review"

    id = Column(Integer,primary_key=True,index=True)
    appraisers_comment_on_workplan = Column(TEXT, nullable=True)
    training_development_comments = Column(TEXT, nullable=True)
    appraisees_comments_and_plan = Column(TEXT, nullable=True)
    head_of_divisions_comments = Column(TEXT, nullable=True)
    appraisal_form_id = Column(Integer, ForeignKey("appraisal_forms.id"))
    performance_details_id = Column(Integer, ForeignKey("performance_details.id"))
    average_per_rating = Column(TEXT, nullable=True)
    average_total = Column(TEXT, nullable=True)
    average_per_rating_id = Column(TEXT, nullable=True)
    end_status = Column(Boolean, default=True, nullable=True)
    submit = Column(Boolean, default=False, nullable=True)
    approval_status = Column(Boolean, default=False, nullable=True)
    created_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
