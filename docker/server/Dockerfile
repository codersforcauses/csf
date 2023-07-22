FROM python:3.11-slim

RUN apt-get update && apt-get install --yes --no-install-recommends postgresql-client g++ libssl-dev && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip && pip install poetry

RUN pip install sendgrid

RUN poetry config virtualenvs.create false

WORKDIR /app

COPY ./docker/server/entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh

COPY ./server/pyproject.toml ./server/poetry.lock ./

RUN poetry install --no-dev

COPY ./server ./
