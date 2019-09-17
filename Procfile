release: python manage.py makemigrations && python manage.py migrate
web gunicorn FastDoWebService.wsgi --log-file -