from aiogram.types import Message
from aiogram.dispatcher import FSMContext

from bot import dp
from state import FormState, FormItem
from components.catalogueList import catalogueList
from utils.fetch import fetch
from constants import CONFIRM_BUTTON_CALLBACK_BRAND_DATA

@dp.message_handler(commands = 'start', state = '*')
async def cmd_start(message: Message, state: FSMContext):
    await state.reset_data()
    await state.reset_state()
    await FormState.withBrands.set()

    brandList: list = fetch('api/params/brands')

    mapedBrandList = list(map(lambda brand: FormItem(brand), brandList))

    await state.update_data(brands = mapedBrandList)
    await message.answer(
        'Поїхали! Оберiть марку авто🚙',
        reply_markup = catalogueList(mapedBrandList, CONFIRM_BUTTON_CALLBACK_BRAND_DATA)
    )
