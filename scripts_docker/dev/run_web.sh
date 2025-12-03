#!/bin/sh
su -m django_user -c "sleep 10 && python manage.py migrate && python manage.py runserver 0.0.0.0:8000"