from sqlalchemy import Column,Integer, String,Boolean, ForeignKey,Date,TIMESTAMP,text
from sqlalchemy.orm import relationship

from database import Base


class Staff(Base):
    '''Staff Model'''
    
    __tablename__ = "staffs"
    staff_id = Column(Integer,primary_key=True,index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    other_name = Column(String, nullable=True)
    gender = Column(String, nullable=True)
    email = Column(String, nullable=False, unique=True, index=True)
    supervisor_id = Column(Integer, nullable=True)
    department = Column(String, nullable=True)
    grade = Column(Integer, nullable=True)
    is_active = Column(Boolean(), default=True)
    is_superuser = Column(Boolean(), default=True)
    created_at = Column(Date, nullable=False)
    updated_at = Column(Date, nullable=False)
    users = relationship("User", back_populates="staff")
    appraisal_forms = relationship("AppraisalForm", back_populates="staffs")

    status = None 