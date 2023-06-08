## core/config.py
## import libraries
import os 
from dotenv import load_dotenv 

from pathlib import Path

## lets load our .env file
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

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
    SECRETE_KEY : str = os.getenv("SECRETE_KEY")
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30
    EMAIL_CODE_DURATION_IN_MINUTES= 15


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