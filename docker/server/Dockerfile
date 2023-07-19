FROM python:3.11-slim

RUN apt-get update && apt-get install --yes --no-install-recommends postgresql-client g++ libssl-dev && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY ./docker/server/entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh

RUN pip install --upgrade pip && pip install poetry

RUN poetry config virtualenvs.create false

COPY ./server/pyproject.toml ./server/poetry.lock ./

RUN poetry install --no-dev

COPY ./server ./
