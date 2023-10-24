## app/main.py
## importing libraries
from starlette.concurrency import run_until_first_complete
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import close_all_sessions
from fastapi.staticfiles import StaticFiles
from services.broadcaster import broadcast
from database import SessionLocal,engine,Database
from fastapi import FastAPI, Request
from scheduler import scheduler
import core.config as cfg
from urls import * 
import os
from routers.users.account.models import User 
from core.hashing import pwd_context


database = Database()
engine = database.get_db_connection()
db = database.get_db_session(engine)


# # ## adding our api routes 
def include_router(app):
    app.include_router(api_router)





uploads: str = os.path.join(os.getcwd(), "core/uploads")
# Create the flyer directory if it doesn't exist
if not os.path.exists(uploads):
        os.makedirs(uploads)






# SEEDING Admin DATA INTO DATABASE
def create_admin(app):
    db_addAdmin = User(email="admin@admin.com",hashed_password=pwd_context.hash("openforme"),is_active=True,user_type_id=1)
    db_email = db.query(User).filter(User.email == "admin@admin.com").first()
    if db_email:
        return "Admin already exist!!!"
    db.add(db_addAdmin)
    db.flush()
    db.commit()
    db.refresh(db_addAdmin)




from routers.users.user_type.models import UserType
# SEEDING UserType DATA INTO DATABASE
def create_usertypes(app):
     add_usertpyes_admin = UserType(title="Admin")
     add_usertpyes_supervisor = UserType(title="Supervisor")
     add_usertpyes_staff = UserType(title="Staff")

     db.add(add_usertpyes_admin)
     db.add(add_usertpyes_supervisor)
     db.add(add_usertpyes_staff)
     db.commit()
     db.refresh(add_usertpyes_admin)
     db.refresh(add_usertpyes_supervisor)
     db.refresh(add_usertpyes_staff)




    
def start_application():
    app = FastAPI(docs_url="/",title=cfg.settings.PROJECT_NAME,version=cfg.settings.PROJECT_VERSION,openapi_url='/openapi.json')
    app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,    
    allow_methods=["*"],
    allow_headers=["*"],
)
    include_router(app)
    create_usertypes(app)
    create_admin(app)
    return app
app = start_application() 

app.mount(cfg.STATIC_URL, StaticFiles(directory=cfg.STATIC_ROOT), name="static")
app.mount(cfg.UPLOAD_URL, StaticFiles(directory=cfg.UPLOAD_ROOT), name="uploads")

@app.on_event("startup")
async def startup_event():
    print('service started')
    scheduler.start()
    await broadcast.connect()

@app.on_event("shutdown")
async def shutdown_event():
    close_all_sessions()
    scheduler.shutdown(wait=False)
    await broadcast.disconnect()

@app.middleware("http")
async def tenant_session(request:Request, call_next):
    db = SessionLocal(bind=engine.execution_options(schema_translate_map={None: request.headers.get('tenant-key'), 'global': request.headers.get('tenant-key')})) if request.headers.get('tenant-key', None) else SessionLocal()
    request.state.db = db
    response = await call_next(request)
    return response