from aiogram.types import Message, CallbackQuery, ParseMode
from aiogram.utils import exceptions

from bot import dp, bot
from utils.errorReport import errorReport

@dp.errors_handler()
async def error(update: CallbackQuery, err):
    await bot.send_message(
        chat_id = update.message.chat.id,
        text = '😬Oops... Seems, we have an error.\n🛠Please, try again later. We are working on this trouble.'
    )

    errorReport(err)
    
    return True
