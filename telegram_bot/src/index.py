import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, executor
from aiogram.types import \
    Message, CallbackQuery, InlineKeyboardButton, \
    InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
from emoji import emojize

from cardList import createBrandList, updateBrandList

load_dotenv()

bot = Bot(token = os.getenv('CHALLENGER_TESTING_TOKEN'))
dp = Dispatcher(bot)

@dp.message_handler(commands = ['start'])
async def start(message: Message):
    await message.answer(
        emojize('Okey! Select car brands :oncoming_automobile:'),
        reply_markup = createBrandList()
    )

@dp.callback_query_handler()
async def selectBrand(callback: CallbackQuery):
    await bot.edit_message_reply_markup(
        chat_id = callback.from_user.id,
        message_id = callback.message.message_id,
        reply_markup = updateBrandList(callback.message.reply_markup, callback.data)
    )

@dp.message_handler(commands = ['help'])
async def help(message: Message):
    await message.reply_markup('<b>/start</b> to create new search')

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates = True)
