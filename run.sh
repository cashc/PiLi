#!/bin/bash

export FLASK_APP=app.py
sudo pigpiod
flask run --host=0.0.0.0
