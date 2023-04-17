FROM python:4.9.6-slim-buster

WORKDIR /app

RUN pip3 install -r requirements.txt --no-cache-dir

COPY ./src .
