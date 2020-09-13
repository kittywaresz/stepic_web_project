#!/bin/sh

sudo /etc/init.d/mysql start

mysql -u root -e "create database stepik_ask_app default character set utf8 default collate utf8_general_ci"
