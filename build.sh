#!/bin/bash

if [ ! -d "env" ]; then
	virtualenv --python=python2.7 env --system-site-packages
	source env/bin/activate
	pip install -I Django==1.9.2
	pip install django-import-export
	pip install djangorestframework
	python manage.py runserver 0.0.0.0:8085
else
	source env/bin/activate
	python manage.py runserver 0.0.0.0:8085
fi
