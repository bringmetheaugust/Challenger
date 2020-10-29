import os
import logging
from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

bot = Bot(token = os.getenv('CHALLENGER_TESTING_TOKEN'))
storage = MemoryStorage()
dp = Dispatcher(bot, storage = storage)
