from sqlalchemy import Column,Integer, String,Boolean, ForeignKey,Date,TIMESTAMP,text
from sqlalchemy.orm import relationship
import uuid
from database import Base
from sqlalchemy.dialects.postgresql import UUID


class Staff(Base):
    '''Staff Model'''
    
    __tablename__ = "staffs"
    #__table_args__ = ({'schema':'public'},)
    
    id = Column(Integer,primary_key=True,index=True)
    first_name = Column(String(255), nullable=True)
    last_name = Column(String(255), nullable=True)
    other_name = Column(String(255), nullable=True)
    #email = Column(String(255), unique=True, index=True)
    department = Column(String(255), nullable=True)
    grade = Column(String(255), nullable=True)
    appointment_date = Column(String(255), nullable=True)
    gender = Column(String(255), nullable=True)
    supervisor_id = Column(Integer, nullable=True)
    user_type_id = Column(Integer, ForeignKey("user_type.id"))
    positions = Column(String(255), nullable=True)
    appraisal_form_id = Column(Integer, ForeignKey("appraisal_forms.id"))
    is_active = Column(Boolean, default=True)
    #is_superuser = Column(Boolean(), default=True)
    status = Column(Boolean, default=False, nullable=True)
    created_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))