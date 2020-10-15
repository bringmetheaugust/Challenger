import os
import logging
from aiogram import Bot, Dispatcher, executor

bot = Bot(token = os.getenv('CHALLENGER_TESTING_TOKEN'))
dp = Dispatcher(bot)

logging.basicConfig(level = logging.INFO)
