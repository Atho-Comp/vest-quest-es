FROM python:latest

WORKDIR /app

COPY ./ ./

RUN pip install Django
