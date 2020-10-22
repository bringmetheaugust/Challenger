from aiogram.types import Message
from aiogram.dispatcher import FSMContext

from bot import dp
from state import FormState, FormItem
from components.catalogueList import catalogueList

carList: list = ['BMW', 'Ford', 'Audi', 'Dodge', 'Reno', 'Volvo', 'Mazda', 'Porshe', 'Lamborgini', 'Lada', 'Opel', 'Chevrole', 'VolzWagen', 'Kia']
years: list = ['2021', '2020', '2019', '2018', '2017', '2016', '2015', '2014', '2013', '2012', '2011', '2010', '2009', '2008']

@dp.message_handler(commands = 'start', state = '*')
async def cmd_start(message: Message, state: FSMContext):
    await state.reset_data()
    await state.reset_state()
    await FormState.withBrands.set()

    mapedBrandList = list(map(lambda brand: FormItem(brand), carList))

    await state.update_data(brands = mapedBrandList)
    await message.answer(
        'Select car brands🚐🚗🚙',
        reply_markup = catalogueList(mapedBrandList)
    )
