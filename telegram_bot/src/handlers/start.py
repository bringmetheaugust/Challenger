from aiogram.types import Message
from aiogram.dispatcher import FSMContext

from bot import dp
from state import FormState, FormItem
from components.catalogueList import catalogueList

carList: list = ['BMW', 'Ford', 'Audi', 'Dodge', 'Reno', 'Volvo', 'Mazda', 'Porshe', 'Lamborgini', 'Lada', 'Opel', 'Chevrole', 'VolzWagen', 'Kia']

@dp.message_handler(commands='start')
async def cmd_start(message: Message, state: FSMContext):
    await FormState.withBrands.set()

    mapedBrandList = list(map(lambda brand: FormItem(brand), carList))

    await state.update_data(brands = mapedBrandList)
    await message.answer(
        'Select car brands🚐🚗🚙',
        reply_markup = catalogueList(mapedBrandList)
    )
