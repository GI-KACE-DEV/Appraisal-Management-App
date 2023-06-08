## app/main.py
## importing libraries
from starlette.concurrency import run_until_first_complete
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import close_all_sessions
from fastapi.staticfiles import StaticFiles
#from services.broadcaster import broadcast
from database import SessionLocal, engine
from fastapi import FastAPI, Request

#from scheduler import scheduler
from config import *
from urls import * 
## 

## adding our api routes 
def include_router(app):
    app.include_router(api_router)

# app = FastAPI(
#     docs_url=None, 
#     redoc_url=None,
#     title=settings.PROJECT_NAME,
#     version=settings.PROJECT_VERSION,
#     openapi_url='/openapi.json'
# )


# app.add_middleware(
#     CORSMiddleware,
#     allow_credentials = True,
#     allow_origins = cfg.ORIGINS,
#     allow_methods = cfg.METHODS,
#     allow_headers = cfg.HEADERS,
# )

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

#app.mount(cfg.STATIC_URL, StaticFiles(directory=cfg.STATIC_ROOT), name="static")
#app.mount(cfg.UPLOAD_URL, StaticFiles(directory=cfg.UPLOAD_ROOT), name="upload")

# @app.on_event("startup")
# async def startup_event():
#     print('service started')
#     scheduler.start()
#     await broadcast.connect()

# @app.on_event("shutdown")
# async def shutdown_event():
#     close_all_sessions()
#     scheduler.shutdown(wait=False)
#     await broadcast.disconnect()

# @app.middleware("http")
# async def tenant_session(request:Request, call_next):
#     db = SessionLocal(bind=engine.execution_options(schema_translate_map={None: request.headers.get('tenant-key'), 'global': request.headers.get('tenant-key')})) if request.headers.get('tenant-key', None) else SessionLocal()
#     request.state.db = db
#     response = await call_next(request)
#     return response

#from core.urls import *
def start_application():
    app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
    include_router(app)
    return app
app = start_application()