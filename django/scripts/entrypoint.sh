#!/bin/bash
##set -o errexit
##set -o pipefail
##set -o nounset
#postgres_ready() {
#    python << END
#import sys
#from psycopg2 import connect
#from psycopg2.errors import OperationalError
#try:
#    connect(
#        dbname="${POSTGRES_DB}",
#        user="${POSTGRES_USER}",
#        password="${POSTGRES_PASSWORD}",
#        host="${POSTGRES_HOST}",
#        port="5432",
#    )
#except OperationalError:
#    sys.exit(-1)
#END
#}
#redis_ready() {
#    python << END
#import sys
#from redis import Redis
#from redis import RedisError
#try:
#    redis = Redis.from_url("${CELERY_BROKER_URL}", db=0)
#    redis.ping()
#except RedisError:
#    sys.exit(-1)
#END
#
#until postgres_ready; do
#  >&2 echo "Waiting for PostgreSQL to become available..."
#  sleep 5
#done
#>&2 echo "PostgreSQL is available"


##until redis_ready; do
##  >&2 echo "Waiting for Redis to become available..."
##  sleep 5
#done
#>&2 echo "Redis is available"
# Section 3- Idempotent Django commands
#python /inventory/manage.py collectstatic --noinput
#python /inventory/manage.py makemigrations
#python /inventory/manage.py migrate
#python /inventory/manage.py runserver 0.0.0.0:8000

exec "$@"

#for (( ; ; ));do
#        sleep 50
#done

