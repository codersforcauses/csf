FROM python:3.11-slim

WORKDIR /documentation

COPY ./documentation ./

RUN pip install mkdocs-material

CMD ["mkdocs","serve","--dev-addr","0.0.0.0:8000"]