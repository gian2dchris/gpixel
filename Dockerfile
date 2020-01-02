FROM python:3.8.1-alpine as builder

# Initialize enviroment
RUN apk update && apk add --no-cache git

RUN mkdir -p /var/www/app

WORKDIR /var/www/gpixel

COPY . ./

# Install dependencies
RUN pip install -r requirements.txt

# Run App
CMD [ "python", "manage.py runserver 0.0.0.0:8000" ]
