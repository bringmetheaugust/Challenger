from aiogram.types import Message, ParseMode

from bot import dp

HELP_MESSAGE: str = '\
/start to create new search. \n\
/stop to stop searching and delete created search. \n\
\n\
All bot\'s info You can find in the bot description.\
'

@dp.message_handler(commands = ['help'])
async def help(message: Message):
    await message.answer(text = HELP_MESSAGE, parse_mode = ParseMode.MARKDOWN)
