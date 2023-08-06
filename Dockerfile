FROM python:3.9-slim-buster

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN apt-get update && apt-get install -y \
    libpq-dev \
    && apt-get -y clean

WORKDIR /usr/src/app

COPY ./requirements.txt /usr/src/app
COPY ./requirements-dev.txt /usr/src/app

RUN pip install --upgrade pip && pip install -r requirements.txt && pip install -r requirements-dev.txt

COPY . /usr/src/app/
