from aiogram.types import CallbackQuery
import re

from bot import dp, bot
from components.catalogueList import updateCatalogueList
from constants import CALLBACK_QUERY_TYPE

@dp.callback_query_handler(lambda callback: re.match(r'brand', callback.data))
async def selectBrand(callback: CallbackQuery):
    await bot.edit_message_reply_markup(
        chat_id = callback.from_user.id,
        message_id = callback.message.message_id,
        reply_markup = updateCatalogueList(callback.message.reply_markup, callback.data)
    )
