from aiogram.types import Message, ParseMode

from bot import dp

@dp.message_handler(commands = 'help', state = '*')
async def help(message: Message):
    await message.answer(
        text = '/start створити новий пошук.\n/зупинити пошук та видалити активний пошук.\n\nПовну iнформацiю Ви знайдете в шапцi бота.',
        parse_mode = ParseMode.MARKDOWN
    )
