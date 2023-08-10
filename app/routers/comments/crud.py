from fastapi.exceptions import HTTPException
from fastapi import status
from sqlalchemy.orm import Session
from routers.comments.model import Comments
from routers.comments.schema import CreateComments




async 