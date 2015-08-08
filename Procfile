web: gunicorn thisishill.wsgi --workers $WEB_CONCURRENCY --preload --access-logfile - --access-logformat '%(t)s "%(r)s" %(s)s %(b)s'
dev-web: gunicorn thisishill.wsgi --workers $WEB_CONCURRENCY --preload --access-logfile - --access-logformat '%(t)s "%(r)s" %(s)s %(b)s'
# worker: celery worker --app thisishill --loglevel info --concurrency=10