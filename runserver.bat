pip install -r .\requirements.txt
python manage.py makemigrations
python manage.py migrate --run-syncdb
python manage.py runserver