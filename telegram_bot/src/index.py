from dotenv import load_dotenv
from aiogram import executor
from aiogram.types import CallbackQuery

load_dotenv()

from bot import dp, bot
import commands
from components.catalogueList import updateCatalogueList

@dp.callback_query_handler()
async def selectBrand(callback: CallbackQuery):
    await bot.edit_message_reply_markup(
        chat_id = callback.from_user.id,
        message_id = callback.message.message_id,
        reply_markup = updateCatalogueList(callback.message.reply_markup, callback.data)
    )

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates = True)
