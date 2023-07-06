## core/config.py
## import libraries
import os 
from dotenv import load_dotenv 

from pathlib import Path

## lets load our .env file
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)


BASE_DIR = Path(__file__).resolve().parent

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

class Settings:
    PROJECT_NAME:str = "Appraisal Management System"
    PROJECT_VERSION: str = "1.0.0"

    POSTGRES_USER: str = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_SERVER: str = os.getenv("POSTGRES_SERVER", "localhost")
    POSTGRES_PORT: str = os.getenv("POSTGRES_PORT", 5432)
    POSTGRES_DB: str = os.getenv("POSTGRES_DB", "appraisal_db")

    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"

    #DATABASE_URL = "mysql+pymysql://root:@localhost:3307/appraisal_db"
    #SECRET_KEY = "supersecretkeyhere"

    ## lets define var for creating the access token
    #SECRET_KEY : str = os.getenv("SECRET_KEY")
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30
    EMAIL_CODE_DURATION_IN_MINUTES= 15
    EMAIL_CODE_DURATION_IN_MINUTES: int = 15
    ACCESS_TOKEN_DURATION_IN_MINUTES: int = 60
    REFRESH_TOKEN_DURATION_IN_MINUTES: int = 600
    PASSWORD_RESET_TOKEN_DURATION_IN_MINUTES: int = 15
    ACCOUNT_VERIFICATION_TOKEN_DURATION_IN_MINUTES: int = 15


    MAIL_USERNAME: str = 'obwebsitedesign@gmail.com'
    MAIL_PASSWORD: str = 'mqzcxllgcoprfxia'
    MAIL_FROM: str = 'obwebsitedesign@gmail.com'
    MAIL_PORT: int = 587
    MAIL_SERVER: str = 'smtp.gmail.com'
    MAIL_STARTTLS = True
    MAIL_SSL_TLS = False
    USE_CREDENTIALS = True
    VALIDATE_CERTS = True


settings = Settings()