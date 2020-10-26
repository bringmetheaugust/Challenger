from aiogram.types import Message
from aiogram.dispatcher import FSMContext

from bot import dp
from state import FormState, FormItem
from components.catalogueList import catalogueList
from utils.fetch import fetch

@dp.message_handler(commands = 'start', state = '*')
async def cmd_start(message: Message, state: FSMContext):
    await state.reset_data()
    await state.reset_state()
    await FormState.withBrands.set()

    res: list = fetch('api/params/brands')

    mapedBrandList = list(map(lambda brand: FormItem(brand), res))

    await state.update_data(brands = mapedBrandList)
    await message.answer(
        'Select car brands🚙',
        reply_markup = catalogueList(mapedBrandList)
    )
