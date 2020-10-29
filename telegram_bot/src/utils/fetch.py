import os
import requests, json
from aiogram.dispatcher.handler import CancelHandler

MAIN_SERVER_URL: str = os.getenv('MAIN_SERVER_URL')
print(MAIN_SERVER_URL)

def fetch(url: str) -> list:
    try:
        res = requests.get(MAIN_SERVER_URL + url)
        responce: list = res.json()
    except:
        CancelHandler()

    return responce
