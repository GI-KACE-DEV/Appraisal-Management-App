## Dockerfile

# pull the official docker image 
FROM python:3.11.1-slim 

# lets set working directory 
WORKDIR /app 

# lets set env variables 
ENV PYTHONDONTWRITEBYTECODE 1 
ENV PYTHONUNBUFFERED 1 

# lets install dependencies 
COPY Pipfile Pipfile.lock /app/
RUN pip install pipenv && pipenv install --system 

## lets copy project 
COPY . /app/