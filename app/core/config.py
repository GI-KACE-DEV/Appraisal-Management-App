## core/config.py
## import libraries
from fastapi.templating import Jinja2Templates
from pydantic import BaseSettings
from datetime import time, date
from functools import lru_cache
import os, logging, config
from dotenv import load_dotenv 
import secrets

from pathlib import Path
from babel import Locale

## lets load our .env file
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)


BASE_DIR = Path(__file__).resolve().parent

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

UPLOAD_URL = "/uploads"
UPLOAD_ROOT = os.path.join(BASE_DIR, 'uploads/')

LOG_ROOT = os.path.join(BASE_DIR, 'logs/')
KEY_ROOT = os.path.join(BASE_DIR, 'x64js/')

AUDIO_ROOT = os.path.join(UPLOAD_ROOT, 'media/audio/')
VIDEO_ROOT = os.path.join(UPLOAD_ROOT, 'media/videos/')
IMAGE_ROOT = os.path.join(UPLOAD_ROOT, 'media/images/')
DOCUMENT_ROOT = os.path.join(UPLOAD_ROOT, 'documents/')

IMAGE_URL = os.path.relpath(IMAGE_ROOT, UPLOAD_ROOT)
VIDEO_URL = os.path.relpath(VIDEO_ROOT, UPLOAD_ROOT)
AUDIO_URL = os.path.relpath(AUDIO_ROOT, UPLOAD_ROOT)
DOCUMENT_URL = os.path.relpath(DOCUMENT_ROOT, UPLOAD_ROOT)

SMALL = (400,400)
LISTQUAD = (250,250)
THUMBNAIL = (128, 128)

UPLOAD_EXTENSIONS = {
    "IMAGE":[".jpeg", ".jpg", ".bmp", ".gif", ".png", ".JPEG", ".JPG", ".BMP", ".GIF", ".PNG",],
    "VIDEO":[".mp4", ".avi", ".mpeg"],
    "AUDIO":[".mp3", ".aac", ".wav"],
    "DOCUMENT":[".pdf", ".csv", ".doc", ".docx", ".eot", ".txt", ".xls", ".xlsx"],
}

ORIGINS = ["*"]
HEADERS = ["*"]
METHODS = ["*"]

JWT_ALGORITHM = 'HS256'

LANGUAGE = "en"

locale = Locale(LANGUAGE)

TEMPLATES = Jinja2Templates(directory=os.path.join(STATIC_ROOT, f'html'))

class Settings:
    PROJECT_NAME:str = "Appraisal Management System"
    PROJECT_VERSION: str = "1.0.0"

    POSTGRES_USER: str = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_SERVER: str = os.getenv("POSTGRES_SERVER", "localhost")
    POSTGRES_PORT: str = os.getenv("POSTGRES_PORT", 5432)
    POSTGRES_DB: str = os.getenv("POSTGRES_DB", "appraisal_db")

    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"


    ## lets define var for creating the access token
    SECRET_KEY : str = os.getenv("SECRET_KEY")
    ALGORITHM = "HS256"
    JWT_SECRET_KEY : str = secrets.token_urlsafe(32)
    ACCESS_TOKEN_EXPIRE_MINUTES = 30
    EMAIL_CODE_DURATION_IN_MINUTES= 15
    EMAIL_CODE_DURATION_IN_MINUTES: int = 15
    ACCESS_TOKEN_DURATION_IN_MINUTES: int = 60
    REFRESH_TOKEN_DURATION_IN_MINUTES: int = 600
    PASSWORD_RESET_TOKEN_DURATION_IN_MINUTES: int = 15
    ACCOUNT_VERIFICATION_TOKEN_DURATION_IN_MINUTES: int = 15


    MAIL_USERNAME: str = 'dev.aiti.com.gh@gmail.com'
    MAIL_PASSWORD: str = 'uefuovgtfwyfgskv'
    MAIL_FROM: str = 'dev.aiti.com.gh@gmail.com'
    MAIL_PORT: int = 587
    MAIL_SERVER: str = 'smtp.gmail.com'
    MAIL_STARTTLS = True
    MAIL_SSL_TLS = False
    USE_CREDENTIALS = True
    VALIDATE_CERTS = True

    APS_COALESCE: bool = False
    APS_MAX_INSTANCES: int = 20
    APS_MISFIRE_GRACE_TIME: int = 4
    APS_THREAD_POOL_MAX_WORKERS: int = 20
    APS_PROCESS_POOL_MAX_WORKERS: int = 5


    # DATABASE_URL = "mysql+pymysql://root:@localhost:3307/appraisal_db"
    # SECRET_KEY = "supersecretkeyhere"

settings = Settings()