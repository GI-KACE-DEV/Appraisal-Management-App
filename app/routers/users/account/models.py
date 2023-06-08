from sqlalchemy import Column, String, Integer, Boolean, ForeignKey, Date
#from mixins import BaseMixin, HashMethodMixin
from sqlalchemy.orm import relationship
from sqlalchemy.orm import validates
#from constants import PHONE, EMAIL
from utils import gen_code
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
    user_type_id = Column(Integer, ForeignKey("user_type.id"))
    department_type_id = Column(Integer, ForeignKey("department_type.id"))
    create_at = Column(Date)
    updated_at = Column(Date)
    reset_password_token = Column(String, nullable=True) 
    satff = relationship("Staff", back_populates="staff")
    department_type = relationship('DepartmentType', back_populates="department_type")
    user_type = relationship("UserType", back_populates="user_type")
    
    @validates('password', include_removes=True)
    def validate_password(self, key, value, is_remove):
        assert len(value) > 7, 'unacceptable password length'
        return self.__class__.generate_hash(value)

    @validates('email')
    def validate_email(self, key, value):
        assert re.search(EMAIL, value), 'invalid email format'
        return value

    @validates('phone')
    def validate_phone(self, key, value):
        assert re.search(PHONE, value), 'invalid phone format'
        return value

    def full_name(self):
        return f'{self.first_name} {f"{self.middle_name} "}{self.last_name}'

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

    @validates('password', include_removes=True)
    def validate_password(self, key, value, is_remove):
        assert len(value) > 7, 'unacceptable password length'
        return self.__class__.generate_hash(value)

    @validates('email')
    def validate_email(self, key, value):
        assert re.search(EMAIL, value), 'invalid email format'
        return value
    
    status = None


    