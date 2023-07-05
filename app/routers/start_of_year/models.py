from sqlalchemy import Column,Integer, String,Boolean, ForeignKey,Date,TIMESTAMP,text
from sqlalchemy.orm import relationship

from database import Base


class StartOfYear(Base):
    '''Start of Year Model'''
    
    __tablename__ = "start_of_year"
    #__table_args__ = ({'schema':'public'},)

    id = Column(Integer,primary_key=True,index=True)
    results_areas = Column(String(255), nullable=True)
    target = Column(String(255), nullable=True)
    resources = Column(String(255), nullable=True)
    appraisal_form_id = Column(Integer, ForeignKey("appraisal_forms.id"))
    start_status = Column(Boolean, default=True, nullable=True)
    submit = Column(Boolean, default=False, nullable=True)
    start_of_year_status = Column(Boolean, default=False, nullable=True)
    created_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    #staffs = relationship("Staff", back_populates="appraisal_forms")