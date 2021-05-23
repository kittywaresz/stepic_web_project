#!/bin/sh

python3 ask/manage.py makemigrations
python3 ask/manage.py migrate
