import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, executor, types

load_dotenv()

bot = Bot(token = os.getenv('CHALLENGER_TESTING_TOKEN'))
dp = Dispatcher(bot)

@dp.message_handler(commands = ['start'])
async def echo(message: types.Message):
    await message.reply(message.text)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
