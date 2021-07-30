#syntax=docker/dockerfile:1

#set base image (host OS)
FROM python:3.9.6-slim-buster

#copy the dependencies file
COPY requirements.txt .

#install dependencies
RUN pip install -r requirements.txt

#copy app & test folders to app & test docker's env
COPY ./test /test
COPY ./app /app

#run the command to start the server
CMD [ "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "15400" ]