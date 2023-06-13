FROM python:3.11-slim

WORKDIR /app

RUN pip install --upgrade pip && pip install poetry

COPY ./server ./

RUN poetry config virtualenvs.create false

RUN poetry install

COPY ./docker/server/entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh

# ENTRYPOINT [ "/entrypoint.sh" ]
