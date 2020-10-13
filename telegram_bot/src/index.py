import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, executor, types
from emoji import emojize

load_dotenv()

carList = ['BWM', 'Ford', 'Audi', 'Dodge']

bot = Bot(token = os.getenv('CHALLENGER_TESTING_TOKEN'))
dp = Dispatcher(bot)

@dp.message_handler(commands = ['start'])
async def echo(message: types.Message):
    # keys = types.InlineKeyboardMarkup()
    # keys.add(list(carList))

    carMenu = types.ReplyKeyboardMarkup()
    carMenu.add(types.InlineKeyboardMarkup())

    # poll_keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
    # poll_keyboard.add(types.KeyboardButton(
    #     text="Создать викторину",
    #     request_poll=types.KeyboardButtonPollType(type = types.PollType.QUIZ))
    # )
    # poll_keyboard.add(types.KeyboardButton(text="Отмена"))

    await message.answer(emojize('Select car\'s brand:oncoming_automobile:'))

@dp.message_handler(commands = ['help'])
async def help(message: types.Message):
    await message.reply_markup('<b>/start</b> to create new search')

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
