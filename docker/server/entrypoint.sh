#!/bin/bash

# Wait until Database is available before continuing
printf "\n" && echo "Checking Database is up"
# using psql
while ! pg_isready -q -h $POSTGRES_HOST -p $POSTGRES_PORT -U $POSTGRES_USER
do
  echo "$(date) - waiting for database to start"
  sleep 1
done

>&2 echo "Postgres is up - continuing"

echo "Applying database migrations"
python manage.py migrate --noinput

echo "Collecting static files"
python manage.py collectstatic --noinput

# Create Django Superuser
echo "Creating Django Superuser"
python manage.py create_superuser --username $DJANGO_SUPERUSER_USERNAME --password $DJANGO_SUPERUSER_PASSWORD

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
    printf "\n" && echo " Running Gunicorn / Django"
    echo "Running: gunicorn api.wsgi -b 0.0.0.0:8081 --workers=6 --keep-alive 20 --log-file=- --log-level debug --capture-output --timeout 50"
    gunicorn api.wsgi -b 0.0.0.0:8081 --workers=6 --keep-alive 20 --log-file=- --log-level debug --capture-output --timeout 50
fi