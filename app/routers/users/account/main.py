from fastapi import APIRouter, Depends,  HTTPException, status


from typing import List
from dependencies import get_db
from sqlalchemy.orm import Session
from . import crud, schemas

user_acc_router = APIRouter()

# @user_acc_router.post("/create", response_model=schemas.ShowUser)
# def create_user(user: schemas.CreateUser, db: Session = Depends(get_db)):
#     user = crud.create_new_user(user=user, db=db)
#     return user 

## lets read a single user from the db
@user_acc_router.get("/get/{id}", response_model=schemas.ShowUser)
def read_user(id:int, db:Session = Depends(get_db)):
    user = crud.retreive_user(id=id, db=db)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Job with this id {id} does not exist")
    return user 

# ## lets list all users in the db
# @user_acc_router.get("/all", response_model=List[schemas.ShowUser])
# def read_users(db: Session = Depends(get_db)):
#     users = crud.list_users(db=db)
#     return users 

# ## 
# @user_acc_router.put('/get/id', response_model=schemas.ShowUser)
# def update_user(id:int, user: schemas.UpdateUser, db: Session = Depends(get_db)):
#     current_user = 1
#     message = crud.update_job_by_id(id=id, user=user, db=db,owner_id=current_user)
#     if not message:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
#         detail=f"Job with id {id} not found.")
#     return {"msg": "Successfully updated data."}

# @user_acc_router.delete('/get/id', response_model=schemas.ShowUser)
# def delete_user(id:int, db: Session = Depends(get_db)):
#     current_user_id = 1
#     message = crud.delete_job_by_id(id=id, db=db, owner_id=current_user_id)
#     if not message:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
#         detail=f"Job with id {id} not found.")
#     return {"msg": "Successfully deleted."}

