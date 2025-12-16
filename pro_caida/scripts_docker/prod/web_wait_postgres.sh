#!/bin/sh
#wait for Postgres to start
postgres_ready() {
  python << END
import sys
import psycopg2
import os
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

>&2 echo "Postgres is up - executing run_web.sh"
sh /code/scripts_docker/prod/run_web.sh