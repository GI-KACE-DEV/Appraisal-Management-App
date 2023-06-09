from sqlalchemy.orm import Session 


from routers.users.account.models import User

def get_user(username:str,db: Session):
    user = db.query(User).filter(User.email == username).first()
    return user

# async def verify_user(payload:schemas.Login, account:str, db:Session):

#     model = User if account=="users" else Administrator        
#     user = db.query(model).filter_by(email=payload.email).first()

#     if not user:
#         raise HTTPException(status_code=404, detail=raise_exc("email", "user not found", "NotFound"))
#     if user.verify_hash(payload.password, user.password):
#         return user
#     raise HTTPException(status_code=401, detail=raise_exc("password", "wrong credentials", "Unauthorized"))
    
#     # except Exception as e:
#     #     print(e)

