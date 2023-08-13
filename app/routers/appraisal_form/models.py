from sqlalchemy import Column,Integer, String,Boolean, ForeignKey,Date,TIMESTAMP,text
import datetime
from sqlalchemy.orm import relationship
import uuid
from database import Base




class AppraisalForm(Base):
    '''Appraisal Form Model'''
    
    __tablename__ = "appraisal_forms"

    id = Column(String(255), primary_key=True,index=True, nullable=False, default=uuid.uuid4)
    department = Column(String(255), nullable=True)
    grade = Column(String(255), nullable=True)
    positions = Column(String(255), nullable=True)
    appraisal_year = Column(String(255), nullable=True)
    staff_id = Column(String(255), ForeignKey("staffs.id"))
    status = Column(Boolean, default=False, nullable=True)
    created_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))

















class Appraisalview(Base):
    '''Appraisal view Model'''
    
    __tablename__ = "appraisal_view"

    id = Column(String(255), primary_key=True,index=True, nullable=False, default=uuid.uuid4)
    first_name = Column(String(255), nullable=True)
    last_name = Column(String(255), nullable=True)
    email = Column(String(255), unique=True, index=True)
    department = Column(String(255), nullable=True)
    grade = Column(String(255), nullable=True)
    gender = Column(String(255), nullable=True)
    supervisor_id = Column(String(255), nullable=True)
    user_type_id = Column(String(255), ForeignKey("user_type.id"))
    positions = Column(String(255), nullable=True)
    appraisal_year = Column(String(255))
    appraisal_form_id = Column(String(255), ForeignKey("appraisal_forms.id"))
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean(), default=True)
    reset_password_token = Column(String(255), nullable=True)
    status = Column(Boolean, default=False, nullable=True)
    created_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))








# class StartOfYear(Base):
#     '''Start of Year Model'''
    
#     __tablename__ = "start_of_year"
#     #__table_args__ = ({'schema':'public'},)

#     id = Column(String(255), primary_key=True,index=True, nullable=False, default=uuid.uuid4)
#     results_areas = Column(String(255), nullable=True)
#     target = Column(String(255), nullable=True)
#     resources = Column(String(255), nullable=True)
#     appraisal_form_id = Column(Integer, ForeignKey("appraisal_forms.id"))
#     start_status = Column(Boolean, default=False, nullable=True)
#     submit = Column(Boolean, default=False, nullable=True)
#     start_of_year_status = Column(Boolean, default=False, nullable=True)
#     created_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
#     updated_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
#     #staffs = relationship("Staff", back_populates="appraisal_forms")
