#!/bin/sh

sudo apt update
sudo apt install python3.5 -y
sudo apt install python3.5-dev -y
sudo apt-get install mysql-server-5.6 -y

sudo unlink /usr/bin/python3
sudo ln -s /usr/bin/python3.5 /usr/bin/python3

sudo python3 -m pip install -r requirements.txt
