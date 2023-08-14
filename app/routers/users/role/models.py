from sqlalchemy import Column, String, event, Integer, ForeignKey, delete
from exceptions import OperationNotAllowed
from sqlalchemy.orm import relationship
from core.config import STATIC_ROOT
#from mixins import BaseMixin
from database import Base
import json, os
import uuid
from sqlalchemy.dialects.postgresql import UUID

class RolePermission(Base):
    '''Role Permission Model'''
    __tablename__ = "role_permissions"
 
    role_id = Column(Integer,primary_key=True,index=True)
    permission_id = Column(Integer, ForeignKey('permissions.id'))

class Role(Base):
    '''Roles Model'''
    __tablename__ = "roles"

    id = Column(Integer,primary_key=True,index=True)
    title = Column(String(255), nullable=False)
    description = Column(String(255), nullable=True)
    #users = relationship('User', back_populates="role")
    permissions = relationship('Permission', back_populates="roles")
    
    def has_perm(self, perm):
        return perm in [perm.id for perm in self.permissions]

    def add_perm(self, perm, db):
        db.add_all([RolePermission(role_id=self.id, permission_id=pid) for pid in perm if not self.has_perm(pid) and self.perm_exists(pid)])
        db.commit()

    def remove_perm(self, perm, db):
        db.query(RolePermission).filter(RolePermission.permission_id.in_(perm), RolePermission.role_id==self.id).delete()
        db.commit()
    
    def clear_perm(self, db):
        self.permissions.clear()
        db.commit() 

    @staticmethod
    def perm_exists(perm):
        from routers.users.permission.models import Permission
        return Permission.query.get(perm) is not None
    
def after_create(target, connection, **kw):

    with open(os.path.join(STATIC_ROOT, 'json/seeds/roles.json')) as file:
        messages = json.load(file)  
        file.close()

    connection.execute(
        Role.__table__.insert(), 
        messages
    )

def after_create_role_permissions(target, connection, **kw):

    with open(os.path.join(STATIC_ROOT, 'json/seeds/role_permissions.json')) as file:
        messages = json.load(file)  
        file.close()

    connection.execute(
        RolePermission.__table__.insert(), 
        messages
    )

# event.listen(Role.__table__, 'after_create', after_create)
# event.listen(RolePermission.__table__, 'after_create', after_create_role_permissions)


# @event.listens_for(Role.title, 'set', propagate=True)
# def receive_set(target, value, oldvalue, initiator):
#     if oldvalue=='Tenant Administrator' and value!=oldvalue:
#         raise OperationNotAllowed('cannot update this property')
