# pull official base image
FROM python:3.8.0-alpine

# Initialize enviroment
RUN apk update && apk add --no-cache git postgresql-dev gcc python3-dev musl-dev

WORKDIR /usr/src/gpixel

# set environment variables
#prevents python from writing .pyc
ENV PYTHONDONTWRITEBYTECODE 1
#prevents buffering stdout/stderr
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

# copy entrypoint.sh
COPY ./entrypoint.sh /usr/src/app/entrypoint.sh

# copy project
COPY . /usr/src/gpixel

# run entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
