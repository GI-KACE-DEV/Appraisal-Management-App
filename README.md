## Project Description

## Environment Configure 
- Installing virtual Env
    - pip install pipenv 

- Installing Packages
    - Using Requirement file
        - pipenv install -r requirement.txt
    - Using the Pipfile
        - Change the python version on your local machine 
        - pipenv install 

- Starting Virtual Env
    - pipenv shell 

- Running FastAPI Service Locally 
    - uvicorn app.main:app --reload

- Running FastAPI Service On Docker 
    - Start Docker Service 
    - docker-compose build
    - docker-compose up -d




    Setup environment variables; allowed environment variables `KEYWORDS`=`VALUES`:

| KEYWORDS | VALUES | DEFAULT VALUE | VALUE TYPE | 
| :------------ | :---------------------: | :------------------: | :------------------: |
| DB_TYPE | | postgresql | string 
| DB_NAME | | appraisal_db | string 
| DB_USER | | postgres | string 
| DB_PASSWORD | | paasword | string 
| DB_PORT | | 5432 | integer   
| BASE_URL | | http://localhost:8000/ | string  
| ADMIN_EMAIL | | admin@admin.com | string 
| ADMIN_PASSWORD | | password | string 
<!-- | EMAIL_CODE_DURATION_IN_MINUTES | | 15 | integer 
| ACCESS_TOKEN_DURATION_IN_MINUTES | | 60 | integer 
| REFRESH_TOKEN_DURATION_IN_MINUTES | | 600 | integer 
| PASSWORD_RESET_TOKEN_DURATION_IN_MINUTES | | 15 | integer 
| ACCOUNT_VERIFICATION_TOKEN_DURATION_IN_MINUTES | | 15 | integer 
| MAIL_USERNAME | | | string 
| MAIL_PASSWORD | | | string 
| MAIL_FROM | | | string 
| MAIL_PORT | | | string 
| MAIL_SERVER | | | string 
| MAIL_FROM_NAME | | | string 
| MAIL_TLS |  boolean 
| MAIL_SSL | | false | boolean 
| USE_CREDENTIALS |  boolean 
| VALIDATE_CERTS |  boolean 
| DEFAULT_MAIL_SUBJECT | | | string  -->


For more info on Fastapi: [Click here](https://fastapi.tiangolo.com/)