from sqlalchemy import Column, String, Integer, Boolean, ForeignKey, Date, TIMESTAMP, text

from sqlalchemy.orm import relationship, validates

from constants import PHONE, EMAIL
from database import Base
import re, uuid

#class User(BaseMixin, HashMethodMixin, Base)
class User(Base):
    '''User Model'''

    __tablename__ = "users"
    #__table_args__ = ({'schema':'public'},)

    id = Column(Integer,primary_key=True,index=True)  
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String,nullable=True)
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean(), default=True)
    created_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    reset_password_token = Column(String, nullable=True)
    staff_id = Column(Integer, ForeignKey("staffs.id"))
    #role_id = Column(Integer, ForeignKey('roles.id'), nullable=True)
    staff = relationship("Staff", back_populates="user")
    #role = relationship("Role", back_populates="users")
    
    @validates('password', include_removes=True)
    def validate_password(self, key, value, is_remove):
        assert len(value) > 7, 'unacceptable password length'
        return self.__class__.generate_hash(value)

    @validates('email')
    def validate_email(self, key, value):
        assert re.search(EMAIL, value), 'invalid email format'
        return value

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


    