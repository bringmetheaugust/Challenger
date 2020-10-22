from aiogram.types import Message, ParseMode

from bot import dp

@dp.message_handler(commands = 'help', state = '*')
async def help(message: Message):
    await message.answer(
        text = '/start to create new search.\n/stop to stop searching and delete created search.\n\nAll bot info You can find in the bot description.',
        parse_mode = ParseMode.MARKDOWN
    )
