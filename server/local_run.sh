#!/bin/sh

source py_env/bin/activate &&
export FLASK_APP=src/index.py &&
flask run --host=0.0.0.0 --port=2101
