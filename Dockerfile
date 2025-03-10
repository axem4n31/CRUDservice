FROM python:3.11

ENV PYTHONUNBUFFERED 1

# Создание и переход в рабочую директорию

WORKDIR /server/

COPY requirements.txt requirements.txt
COPY . .

RUN pip install -r requirements.txt