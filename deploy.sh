#!/bin/bash

# Collect static files
python manage.py collectstatic --noinput

# Apply migrations
python manage.py migrate

# Start Gunicorn server
gunicorn myproject.wsgi:application --bind 0.0.0.0:8000 