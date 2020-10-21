from dotenv import load_dotenv
from aiogram import executor

load_dotenv()

from bot import dp
import state
import handlers

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates = True)
