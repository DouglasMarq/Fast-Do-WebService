release: python manage.py makemigrations --noinput && python manage.py migrate
web gunicorn FastDoWebService.wsgi --log-file -