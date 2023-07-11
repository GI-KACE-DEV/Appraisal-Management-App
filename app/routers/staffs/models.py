from sqlalchemy import Column,Integer, String,Boolean, ForeignKey,Date,TIMESTAMP,text
from sqlalchemy.orm import relationship

from database import Base


class Staff(Base):
    '''Staff Model'''
    
    __tablename__ = "staffs"
    #__table_args__ = ({'schema':'public'},)
    
    id = Column(Integer,primary_key=True,index=True)
    first_name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)
    other_name = Column(String(255), nullable=True)
    gender = Column(String(255), nullable=True)
    supervisor_id = Column(Integer, nullable=True)
    department = Column(String(255), nullable=True)
    positions = Column(String(255), nullable=True)
    appointment_date = Column(String(255), nullable=True)
    grade = Column(Integer, nullable=True)
    is_active = Column(Boolean(), default=True)
    is_superuser = Column(Boolean(), default=True)
    created_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    #user = relationship("User", back_populates="staff")
    #appForm_id = Column(Integer, ForeignKey("appraisal_forms.appform_id"))
    #appraisal_forms = relationship("AppraisalForm", back_populates="staffs")

    status = None 