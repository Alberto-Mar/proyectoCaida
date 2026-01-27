#!/bin/sh
exec su -m django_user -c "gunicorn --chdir /code/laCaida --bind 0.0.0.0:8000 laCaida.wsgi:application"