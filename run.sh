#!/bin/bash
if [ "$1" != "-d" ]; then
    export FLASK_DEBUG=1
fi
export FLASK_APP=/home/cashc/PiLi/app.py
sudo pigpiod
flask run --host=0.0.0.0
