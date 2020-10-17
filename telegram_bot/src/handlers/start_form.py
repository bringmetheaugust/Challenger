from aiogram.types import CallbackQuery

from bot import dp, bot
from components.catalogueList import updateCatalogueList
from constants import BRAND_CALLBACK_QUERY_TYPE, CONFIRM_BUTTON_CALLBACK_QUERY_TYPE

@dp.callback_query_handler(lambda callback: BRAND_CALLBACK_QUERY_TYPE in callback.data)
async def selectBrand(callback: CallbackQuery):
    await bot.edit_message_reply_markup(
        chat_id = callback.from_user.id,
        message_id = callback.message.message_id,
        reply_markup = updateCatalogueList(callback.message.reply_markup, callback.data)
    )

# @dp.callback_query_handler(lambda callback: CONFIRM_BUTTON_CALLBACK_QUERY_TYPE in callback.data)
# async def confirmBrand(callback: CallbackQuery):
#     print("CONFIRM BUTTON")
#     await callback.answer(text = 'You select cars!!!')
