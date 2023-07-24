FROM python:3.11-slim

RUN pip install mkdocs-material

WORKDIR /documentation

COPY ./documentation ./

CMD ["mkdocs","serve","--dev-addr","0.0.0.0:8000"]