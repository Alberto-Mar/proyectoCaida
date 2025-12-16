#!/bin/sh
exec su -m django_user -c "gunicorn --chdir /code/pro_caida --bind 0.0.0.0:8000 laCaida.wsgi:application"