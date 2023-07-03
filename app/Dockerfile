## Dockerfile

# pull the official docker image 
FROM python:3.10

# lets set working directory 
WORKDIR /app 

# lets set env variables 
ENV PYTHONDONTWRITEBYTECODE 1 
ENV PYTHONUNBUFFERED 1 

## lets copy project 
COPY . /app
# RUN cd /app

# lets install dependencies 
# COPY Pipfile /app
RUN pip install pipenv && pipenv install --system 

EXPOSE 8000
CMD [ "uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000" ]