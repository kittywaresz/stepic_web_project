#!/bin/sh

sudo ln -f -r -s /home/box/web/etc/test.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart

sudo gunicorn -c /home/box/web/etc/gunicorn.conf.py ask.wsgi:application
