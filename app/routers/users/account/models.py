from sqlalchemy import Column, String, Integer, Boolean, ForeignKey, Date

from sqlalchemy.orm import relationship

from database import Base
import re, uuid

#class User(BaseMixin, HashMethodMixin, Base)
class User(Base):
    '''User Model'''

    __tablename__ = "users"
    user_id =Column(Integer,primary_key=True,index=True)  
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String,nullable=False)
    is_active = Column(Boolean, default=False)
    staff_id = Column(Integer, ForeignKey("staff.staff_id"))
    create_at = Column(Date)
    updated_at = Column(Date)
    reset_password_token = Column(String, nullable=True) 
    satff = relationship("Staff", back_populates="staff")
   

    status = None

class Administrator(Base):
    '''System Administrator Model'''
    __tablename__ = "administrators"
    __table_args__ = ({'schema':'public'},)
    
    admin_id =Column(Integer,primary_key=True,index=True) 
    is_active = Column(Boolean, default=False)
    email = Column(String, unique=True, index=True)
    is_verified = Column(Boolean, default=False)
    password = Column(String, nullable=True)
    push_id = Column(String, unique=True, nullable=False, default=uuid.uuid4)

    
    status = None


    