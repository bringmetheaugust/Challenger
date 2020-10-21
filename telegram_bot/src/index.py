from dotenv import load_dotenv
from aiogram import executor

load_dotenv()

from bot import dp
import state
import handlers
from middleWare import UpdateCatalogueMiddleware

if __name__ == "__main__":
    dp.middleware.setup(UpdateCatalogueMiddleware())
    executor.start_polling(dp, skip_updates = True)
