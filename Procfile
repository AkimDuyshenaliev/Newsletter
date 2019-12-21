web: gunicorn Main.wsgi --log-file -
worker: celery worker --app=tasks.app