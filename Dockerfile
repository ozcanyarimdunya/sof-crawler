FROM python:3.7

ENV PYTHONBUFFERED 1

WORKDIR /app

COPY requirements.txt ./requirements.txt

RUN pip install -r requirements.txt

COPY . .