#!/bin/bash

echo "Applying database migrations"
python manage.py migrate --noinput

echo "Starting server"
python manage.py runserver 0.0.0.0:8081
