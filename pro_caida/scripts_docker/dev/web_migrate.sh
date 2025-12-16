#!/bin/sh
postgres_ready() {
python << END
import sys
import os
import psycopg2
POSTGRES_DB = open('/run/secrets/POSTGRES_DB', 'r').read().strip()
POSTGRES_USER = open('/run/secrets/POSTGRES_USER', 'r').read().strip()
POSTGRES_PASSWORD = open('/run/secrets/POSTGRES_PASSWORD', 'r').read().strip()
try:
    conn = psycopg2.connect(dbname=POSTGRES_DB,
        user=POSTGRES_USER,
        password=POSTGRES_PASSWORD,
        host="db"
    )
except psycopg2.OperationalError:
    sys.exit(-1)
sys.exit(0)
END
}
until postgres_ready; do
 >&2 echo "Postgres is unavailable - sleeping"
 sleep 1
done
if [ "$MAKEMIGRATIONS" = "yes" ]; then
  >&2 echo "Postgres is up - makemigrations "
  su -m django_user -c "python manage.py makemigrations --noinput"
fi

if [ "$MIGRATE" = "yes" ]; then
  >&2 echo "Postgres is up - migrate "
  su -m django_user -c "python manage.py migrate --noinput"
fi

if [ "$STATIC" = "yes" ]; then
  >&2 echo "Postgres is up - collecting static"
  su -m django_user -c "python manage.py collectstatic --noinput"
fi