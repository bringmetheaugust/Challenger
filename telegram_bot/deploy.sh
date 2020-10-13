#!/bin/sh

python3 -m venv py_env &&
source py_env/bin/activate &&
pip install -U aiogram &&
pip install -U pylint &&
pip install -U python-dotenv &&
pip install -U emoji &&
deactivate
