#!/bin/sh
python manage.py migrate --noinput  # Run migrations
exec "$@"  # Launch main CMD (Gunicorn)
