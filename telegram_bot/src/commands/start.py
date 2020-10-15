from aiogram.types import Message
from emoji import emojize

from bot import dp
from components.catalogueList import createCatalogueList


carList: list = ['BMW', 'Ford', 'Audi', 'Dodge', 'Reno', 'Volvo', 'Mazda', 'Porshe', 'Lamborgini', 'Lada', 'Opel', 'Chevrole', 'VolzWagen', 'Kia']

@dp.message_handler(commands = ['start'])
async def start(message: Message):
    await message.answer(
        emojize('Okey! Select car brands :oncoming_automobile:'),
        reply_markup = createCatalogueList(carList)
    )
