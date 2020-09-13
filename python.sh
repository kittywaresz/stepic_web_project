#!/bin/sh

sudo apt update
sudo apt install python3.5 python3-dev default-libmysqlclient-dev build-essential

sudo rm /usr/bin/python3
sudo ln -s /usr/bin/python3.5 /usr/bin/python3

python -m venv venv
