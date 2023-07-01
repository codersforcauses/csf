#!/bin/bash

# Syncs python env with deps incase container image has not
# been rebuilt with the latest poetry.lock
echo "Installing dependencies"
poetry install

echo "Applying database migrations"
python manage.py migrate --noinput

# Create Django Superuser
echo "Creating Django Superuser"
python manage.py createsuperuser --noinput --username $DJANGO_SUPERUSER_USERNAME --email $DJANGO_SUPERUSER_EMAIL

echo "Starting server"
python manage.py runserver 0.0.0.0:8081
