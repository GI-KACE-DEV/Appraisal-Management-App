from sqlalchemy import Column, String, event
#from mixins import GenCodeMixin, BaseMixin
from sqlalchemy.orm import validates 
from ..account.models import *
#from constants import EMAIL
from database import Base
import re

class EmailVerificationCode(Base):
    '''Email Verification model'''
    __tablename__ = 'email_verication_codes'
    __table_args__ = ({'schema':'public'},)

    email = Column(String, unique=True, primary_key=True)
    
    @validates('email')
    def validate_email(self, key, value):
        assert re.search(EMAIL, value), 'invalid email format'
        return value

class RevokedToken(Base):
    __tablename__ = 'revoked_tokens'
    __table_args__ = ({'schema':'public'},)

    revoke_id = Column(Integer,primary_key=True,index=True) 
    jti = Column(String)

@event.listens_for(EmailVerificationCode, 'before_insert')
def delete_existing_value(mapper, connection, target):
    with connection.begin():
        connection.execute(
            EmailVerificationCode.__table__.delete().where(EmailVerificationCode.__table__.c.email == target.email)
        )