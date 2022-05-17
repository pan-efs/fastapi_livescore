#syntax=docker/dockerfile:1

#set base image (host OS)
FROM python:3.9.6-slim-buster

# Install necessary packages
RUN apt-get update
RUN apt-get install -y --no-install-recommends build-essential \
    gcc \
    git \
    openssh-client

RUN apt-get clean && rm -rf /var/lib/apt/lists/*

# Create the virtual environment to run code within
RUN python3.9 -m venv /venv
ENV PATH=/venv/bin:$PATH

#copy the dependencies file
COPY requirements.txt .

# Install pip requirements
RUN pip install -r requirements.txt

#copy app & test folders to app & test docker's env
COPY ./test /test
COPY ./app /app

#run the command to start the server
CMD [ "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000" ]
