from routers.events.schema import CreateEvent,UpdateEvent
from typing import Any,Dict,Generic,Type,TypeVar,Union
from routers.admin.schema import CreateUser,UpdateUser
from routers.participants.schema import CreateParticipant,UpdateParticipant
from routers.participant_fields.schema import CreateParticipantField,UpdateParticipantField
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from utils.database import Base
from pydantic import BaseModel
from models.models import *






# Define custom types for SQLAlchemy model, and Pydantic schemas
ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)





class BaseActions(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):

    def __init__(self, model: Type[ModelType]):
        self.model = model








# #function to create new data
    def create(self, obj_in: CreateSchemaType, db:Session, **kw):
        obj_in_data = jsonable_encoder(obj_in, **kw)
        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj








#function to read all
    def read(self, db: Session, *, skip: int = 0, limit: int = 100):
        return db.query(self.model).offset(skip).limit(limit).all()
    





## function to get base on id
    def get(self, db: Session, id: str):
        return db.query(self.model).filter(self.model.id == id).first()
    






## function to update base on id
    def update(self,db: Session,*,db_obj: ModelType,obj_in: Union[UpdateSchemaType, Dict[str, Any]]):
        obj_data = jsonable_encoder(db_obj)
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        for field in obj_data:
            if field in update_data:
                setattr(db_obj, field, update_data[field])
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj







## function to remove base on id
    def remove(self, db: Session, *, id: str):
        obj = db.query(self.model).get(id)
        db.delete(obj)
        db.commit()
        return obj
    





## function to get  base on email
    def get_by_email(self, db: Session, email: str):
        return db.query(self.model).filter(self.model.email == email).first()
    





class AdminCRUD(BaseActions[Admin, CreateUser, UpdateUser]):
    pass

