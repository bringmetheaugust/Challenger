from aiogram.types import Message, CallbackQuery, ParseMode
from aiogram.utils import exceptions
from emoji import emojize

from bot import dp, bot

@dp.errors_handler(exception = exceptions.MessageNotModified)
async def notModified(update: CallbackQuery, err):
    await bot.send_message(
        chat_id = update.callback_query.message.chat.id,
        text = emojize(':hushed:Seems, You didn\'t choose anything..', use_aliases = True)
    )
    
    return True
