from os import getenv
import requests, json
from aiogram.dispatcher.handler import CancelHandler

MAIN_SERVER_URL: str = getenv('MAIN_SERVER_URL')

def fetch(url: str) -> list:
    try:
        res = requests.get(MAIN_SERVER_URL + url)
        responce: list = res.json()

        return responce
    except:
        CancelHandler()
