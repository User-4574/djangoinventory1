#!/bin/bash

cd /inventory

if [ $# -eq 0 ]; then
    echo "Usage: start.sh [PROCESS_TYPE](server/beat/worker/flower)"
    exit 1
fi
#function die(){
#    rm -f /inventory/inventorysystem/settings.py
#}
#trap die SIGTERM
PROCESS_TYPE=$1

if [ "$PROCESS_TYPE" = "server" ]; then
    #I would have rather used environment variables in settings.py, but alas, they did not work for some reason, also trapping SIGTERM didn't work either, strangely.
    rm -f /inventory/django_inventory/settings.py
    #/scripts/dockerize -template /inventory/inventorysystem/settings.py.tmpl:/inventory/inventorysystem/settings.py
#    rm -f /inventory/templates/registration/login.html
#    if [ "$SOCIAL_AUTH_ENABLE" = "True" ];then
#        /scripts/dockerize -delims "<<:>>" -template /inventory/templates/registration/login_google_oauth.html.tmpl:/inventory/templates/registration/login.html
#    else
#        cp -f /inventory/templates/registration/login_orig.html /inventory/templates/registration/login.html
#    fi
    #Populate an empty database if no database present.
#    python /inventory/manage.py migrate
    if [ "$DJANGO_DEBUG" = "True" ]; then
        /scripts/dockerize -template /inventory/django_inventory/settings.py.tmpl:/inventory/django_inventory/settings.py 
        python ./manage.py runserver 0.0.0.0:8000
        #So that in dev mode you can kill the server and restart it at your leisure.
        for (( ; ; ));do
            sleep 50
        done
    else
        /scripts/dockerize -template /inventory/django_inventory/settings.py.tmpl:/inventory/django_inventory/settings.py 
	gunicorn \
            --bind 0.0.0.0:8000 \
            --workers 2 \
            --worker-class gevent \
            --log-level DEBUG \
            --access-logfile "-" \
            --error-logfile "-" \
            inventorysystem.wsgi
       for (( ; ; ));do
            sleep 50
        done

    fi
elif [ "$PROCESS_TYPE" = "beat" ]; then
    /scripts/dockerize -wait tcp://${DJANGOHOST}:8000 celery \
        --app django_inventory.celery_app \
        beat \
        --loglevel INFO \
        --scheduler django_celery_beat.schedulers:DatabaseScheduler
elif [ "$PROCESS_TYPE" = "flower" ]; then
    /scripts/dockerize -wait tcp://${DJANGOHOST}:8000 celery \
        --app django_inventory.celery_app \
        flower \
        --basic_auth="${CELERY_FLOWER_USER}:${CELERY_FLOWER_PASSWORD}" \
        --loglevel INFO
elif [ "$PROCESS_TYPE" = "worker" ]; then
    /scripts/dockerize -wait tcp://${DJANGOHOST}:8000 celery \
        --app django_inventory.celery_app \
        worker \
        --loglevel INFO
elif [ "$PROCESS_TYPE" = "nginx" ]; then
	rm -f /etc/nginx/sites-enabled/default
	/scripts/dockerize -template /root/site.conf.tmpl:/etc/nginx/sites-enabled/default -wait tcp://${DJANGOHOST}:8000 nginx -c /etc/nginx/nginx.conf 
    for (( ; ; ));do
        sleep 50
    done

fi
#for (( ; ; ));do
#        sleep 50
#done
