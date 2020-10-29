from dotenv import load_dotenv
from aiogram import executor
print("START")

load_dotenv()

from bot import dp
import state
import handlers
from middleWare import HandlerMiddleware

dp.middleware.setup(HandlerMiddleware())
executor.start_polling(dp, skip_updates = True)
