from sqlalchemy import Column,Integer, String,Boolean, ForeignKey,Date,TIMESTAMP,text
from sqlalchemy.orm import relationship

from database import Base


class AppraisalForm(Base):
    '''Appraisal Form Model'''
    
    __tablename__ = "appraisal_form"
    appraisal_form_id = Column(Integer,primary_key=True,index=True)
    department = Column(String, nullable=True)
    grade = Column(String, nullable=True)
    positions = Column(String, nullable=True)
    appraisal_date = Column(String, nullable=True)
    staff_id = Column(Integer, ForeignKey("staff.staff_id"))
    status = Column(String, nullable=True)
    created_at = Column(TIMESTAMP, nullable=False,server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(TIMESTAMP, nullable=False,server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    satff = relationship("Staff", back_populates="appraisal_form")