#!/bin/bash
cd src
python manage.py makemigrations
until python manage.py migrate; do
  sleep 2
  echo "Retry!";
done

python manage.py makemigrations
python manage.py migrate

python manage.py runserver 0.0.0.0:8000