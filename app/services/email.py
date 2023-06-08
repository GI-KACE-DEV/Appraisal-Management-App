from typing import List
from fastapi_mail import ConnectionConfig, FastMail, MessageSchema, MessageType
from pydantic import BaseModel, EmailStr
from starlette.responses import JSONResponse
from dotenv  import dotenv_values
from config import settings
from routers.staffs.models import Staff



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




async def sendEmailToNewStaff(email: EmailSchema, instance: Staff):



    html = f"""
        <!doctype html>
        <html lang="en">
            <head>
                <title>APPRAISAL FORM</title>
            </head>

            <body>
                <div style="display:flex;align-items:center;justify-content:center;flex-direction:column;">
                    <h3>APPRAISAL FORM</h3>
                    <br>
                    <h3> {instance.last_name} </h3>
                    <p>Please click on the button below to fill your appraisal form</p>

                    <a style="margin-top:1rem;padding:1rem;border-radius:0.5rem;font-size:1rem;text-decoration:none;
                    background: #0275d8; color:white;" href="http://localhost:4200/reset-password">
                    Appraisal Form
                    </a>

                    <p>Please kindly Ignore this email if you are not a GI-KACE staff</p>
                </div>

            </body>
        </html>
    """




    message = MessageSchema(
        subject="APPRAISAL MANAGEMENT SYSTEM",
        recipients=email,
        body=html,
        subtype=MessageType.html
        )

    fm = FastMail(conf)
    await fm.send_message(message)
    return JSONResponse(status_code=200, content={"message": "email has been sent"})