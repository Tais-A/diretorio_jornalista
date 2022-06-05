#!/bin/bash

mkdir -p logs


python manage.py collectstatic
python manage.py makemigrations
python manage.py migrate
#pytest --cov=api api/tests/

# Gunicorn
gunicorn DiretorioJornalistas.wsgi:application \
  --bind 0.0.0.0:8000 \
  --workers 4 --timeout 3600 \
  --log-file=logs/gunicorn_error.log \
  --access-logfile=logs/gunicorn_access.log
