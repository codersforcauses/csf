#!/bin/bash

echo "Applying database migrations"
python manage.py migrate --noinput


# Create Django Superuser
echo "Creating Django Superuser"
python manage.py createsuperuser --noinput --username $DJANGO_SUPERUSER_USERNAME --email $DJANGO_SUPERUSER_EMAIL

echo "Starting server"
python manage.py runserver 0.0.0.0:8081
