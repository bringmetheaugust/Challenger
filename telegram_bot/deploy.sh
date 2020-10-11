#!/bin/sh

python3 -m venv py_env
source py_env/bin/activate
pip install python-telegram-bot --upgrade
pip install -U pylint
deactivate
