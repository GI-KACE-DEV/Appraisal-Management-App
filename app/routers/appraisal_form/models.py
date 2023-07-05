from sqlalchemy import Column,Integer, String,Boolean, ForeignKey,Date,TIMESTAMP,text
from sqlalchemy.orm import relationship

from database import Base


class AppraisalForm(Base):
    '''Appraisal Form Model'''
    
    __tablename__ = "appraisal_forms"
    #__table_args__ = ({'schema':'public'},)

    id = Column(Integer,primary_key=True,index=True)
    department = Column(String, nullable=True)
    grade = Column(String, nullable=True)
    positions = Column(String, nullable=True)
    appraisal_date = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    staff_id = Column(Integer, ForeignKey("staffs.id"))
    status = Column(Boolean, default=False, nullable=True)
    created_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    #staffs = relationship("Staff", back_populates="appraisal_forms")