#!/bin/sh

source py_env/bin/activate &&
nodemon --exec python3 src/index.py
