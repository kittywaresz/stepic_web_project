#bin/sh
# task 1
sudo ln -f -r -s /home/box/web/etc/test.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart

# task 2
# gunicorn -b 0.0.0.0:8080 -c /home/box/web/etc/gunicorn.conf.py hello:app

# task 3
sudo gunicorn -c /home/box/web/etc/gunicorn.conf.py ask.wsgi:application
