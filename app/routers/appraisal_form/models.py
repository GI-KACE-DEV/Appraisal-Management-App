from sqlalchemy import Column,Integer, String,Boolean, ForeignKey,Date,TIMESTAMP,text
from sqlalchemy.orm import relationship

from database import Base


class AppraisalForm(Base):
    '''Appraisal Form Model'''
    
    __tablename__ = "appraisal_forms"
    appraisal_form_id = Column(Integer,primary_key=True,index=True)
    department = Column(String, nullable=True)
    grade = Column(String, nullable=True)
    positions = Column(String, nullable=True)
    appraisal_date = Column(Date, nullable=True)
    staff_id = Column(Integer, ForeignKey("staffs.staff_id"))
    status = Column(String, nullable=True)
    created_at = Column(Date, nullable=False)
    updated_at = Column(Date, nullable=False)
    staffs = relationship("Staff", back_populates="appraisal_forms")