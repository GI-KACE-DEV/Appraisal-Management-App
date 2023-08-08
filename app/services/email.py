from typing import List
from fastapi_mail import ConnectionConfig, FastMail, MessageSchema, MessageType
from pydantic import BaseModel, EmailStr
from starlette.responses import JSONResponse
from dotenv  import dotenv_values
from core.config import settings
from routers.appraisal_form.models import Appraisalview



config_credentials = dotenv_values(".env")



class EmailSchema(BaseModel):
    email: List[EmailStr]


conf = ConnectionConfig(
    MAIL_USERNAME = settings.MAIL_USERNAME,
    MAIL_PASSWORD = settings.MAIL_PASSWORD,
    MAIL_FROM =  settings.MAIL_FROM,
    MAIL_PORT = settings.MAIL_PORT,
    MAIL_SERVER = settings.MAIL_SERVER,
    MAIL_STARTTLS = settings.MAIL_STARTTLS,
    MAIL_SSL_TLS = settings.MAIL_SSL_TLS,
    USE_CREDENTIALS = settings.USE_CREDENTIALS,
    VALIDATE_CERTS = settings.VALIDATE_CERTS
)




async def sendEmailToNewStaff(email: EmailSchema, instance: Appraisalview):


    html = f"""                    
                    <br>
                    <p>Hi {instance.last_name}, {instance.first_name} !</p>
                    <br>
                    <p>You have been added and assigned to <b>GI-KACE APPRAISAL MANAGEMENT SYSTEM</b></p>
                    <br><br>
                    Change your password to access the application.
                    <br><br>
                    
                    <a style="margin-top:1rem;padding:1rem;border-radius:0.5rem;font-size:1rem;text-decoration:none;
                    background: #0275d8; color:white;" href="http://localhost:4200/reset-password?token={instance.reset_password_token}">
                    Change password 
                    </a>
                    <br><br>
                    <p>If you're having problem clicking the Change Password button, copy and paste the URL below into your web browser</p>
                    http://localhost:4200/reset-password?token={instance.reset_password_token}
                    
    """




    message = MessageSchema(
        subject="GI-KACE APPRAISAL MANAGEMENT SYSTEM",
        recipients=email,
        body=html,
        subtype=MessageType.html
        )

    fm = FastMail(conf)
    await fm.send_message(message)
    return JSONResponse(status_code=200, content={"message": "email has been sent"})





































async def send_Reset_Password_LinkToStaffEmail(email: EmailSchema, instance: Appraisalview):

    html = f"""                    
                    <br>
                    <p>Hi {instance.last_name}, {instance.first_name} !</p>
                    <br>
                    <p>You have requested to reset your password. Click on the button below to reset your password</p>

                    <br><br>
                    
                    <a style="margin-top:1rem;padding:1rem;border-radius:0.5rem;font-size:1rem;text-decoration:none;
                    background: #0275d8; color:white;" href="http://localhost:4200/reset-password?token={instance.reset_password_token}">
                    Reset password 
                    </a>
                    <br><br>
                    <p>If you're having problem clicking the Change Password button, copy and paste the URL below into your web browser
                    <br>
                    <b>Link expires in 3 hours</b>
                    </p>
                    http://localhost:4200/reset-password?token={instance.reset_password_token}
                    <br><br>
                    <p><b>Ignore this email if you have not requested to reset your password</b></p>
                    
    """


    message = MessageSchema(
        subject="GI-KACE APPRAISAL MANAGEMENT SYSTEM",
        recipients=email,
        body=html,
        subtype=MessageType.html)

    fm = FastMail(conf)
    await fm.send_message(message)
    return JSONResponse(status_code=200, content={"message": "email has been sent"})