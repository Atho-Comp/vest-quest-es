FROM python:3.9

RUN pip install django 

WORKDIR /app

COPY ./ ./

RUN python manage.py makemigrations
RUN python manage.py migrate
