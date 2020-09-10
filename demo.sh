#!/bin/bash
cd /root
source env/bin/activate
cd /root/demoproject
python manage.py runserver 192.168.199.14:8000 &
echo -ne '\n'
