FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install --yes --no-install-recommends postgresql-client g++ libssl-dev && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip && pip install poetry

COPY ./server ./

RUN poetry config virtualenvs.create false

RUN poetry install --no-dev

COPY ./docker/server/entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh
