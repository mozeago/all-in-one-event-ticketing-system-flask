#!/bin/sh
export FLASK_APP=./flask-event-booking/app.py
pipenv run flask --debug run -h 0.0.0.0