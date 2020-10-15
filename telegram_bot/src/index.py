from dotenv import load_dotenv
from aiogram import executor

load_dotenv()

from bot import dp
from commands import start, stop, help
from handlers import error, start_form

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates = True)
