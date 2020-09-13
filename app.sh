#!/bin/sh

python ask/manage.py makemigrations
python ask/manage.py migrate
