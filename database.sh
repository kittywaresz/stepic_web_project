#!/bin/sh

sudo /etc/init.d/mysql start

mysql -uroot -proot -e "CREATE DATABASE stepik_ask_app;"
mysql -uroot -proot -e "GRANT ALL PRIVILEGES ON stepik_ask_app.* TO 'root'@'localhost' WITH GRANT OPTION;"
