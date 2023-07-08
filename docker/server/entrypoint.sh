#!/bin/bash

echo "Applying database migrations"
python manage.py migrate --noinput

echo "Collecting static files"
python manage.py collectstatic --noinput

# Create Django Superuser
echo "Creating Django Superuser"
python manage.py createsuperuser --noinput --username $DJANGO_SUPERUSER_USERNAME --email $DJANGO_SUPERUSER_EMAIL

# Run inbuilt Django server if ENV is development
if [ "${APP_ENV^^}" = "DEVELOPMENT" ]; then

    # Install extra non-prod packages
    printf "\n" && echo "Installing dev dependencies for $APP_ENV"
    poetry install

    # Run developments
    printf "\n" && echo "Starting inbuilt django webserver"
    echo "Running: python manage.py runserver 0.0.0.0:8081"
    python manage.py runserver 0.0.0.0:8081
    exit
fi

# ===================
# Run Django/Gunicorn
# ===================
if [ "${APP_ENV^^}" = "PRODUCTION" ]; then

    # Run Gunicorn / Django
    printf "\n" && echo " Running Gunicorn / Django" | boxes -d shell -p a1l2
    echo "Running: gunicorn api.wsgi -b 0.0.0.0:8081 --workers=6 --keep-alive 20 --log-file=- --log-level debug --access-logfile=/var/log/accesslogs/gunicorn --capture-output --timeout 50"
    gunicorn api.wsgi -b 0.0.0.0:8081 --workers=6 --keep-alive 20 --log-file=- --log-level debug --access-logfile=/var/log/accesslogs/gunicorn --capture-output --timeout 50
fi