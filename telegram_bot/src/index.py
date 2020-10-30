from dotenv import load_dotenv
from aiogram import executor
# from sys import exit

load_dotenv()

from bot import dp
import state
import handlers
from middleWare import HandlerMiddleware

if __name__ == "__main__":
    dp.middleware.setup(HandlerMiddleware())
    executor.start_polling(dp, skip_updates = True)
