#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi
#Do NOT Run in Production ! Flushes DB !
python manage.py flush --settings=gpixel.settings.base --no-input
python manage.py migrate --settings=gpixel.settings.base

exec "$@"

