#!/bin/sh

echo "Create a virtual environment"
pip install virtualenv
virtualenv virtualenv
source virtualenv/bin/activate
pip install -r requirements.txt

echo "Creating database"
createdb genetica
python manage.py migrate

echo "Start faking data"
python load_data.py

echo "Start testing"
python manage.py test

echo "Testing finish! Do you want to start? (y/n)"
read ans

if [ "$ans" = 'y' ]; then
  python manage.py runserver 0.0.0.0:8000
else
  echo "Stopped!"
fi
