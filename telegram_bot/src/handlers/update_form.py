from aiogram.types import CallbackQuery, InlineKeyboardMarkup
from aiogram.utils import exceptions
from aiogram.dispatcher import FSMContext

from bot import dp, bot
from state import FormState, FormItem
from components.catalogueList import catalogueList

@dp.callback_query_handler(state = FormState.withBrands)
async def selectBrand(callback: CallbackQuery, state: FSMContext):
    await FormState.withYears.set()

@dp.callback_query_handler(state = FormState.withYears)
async def selectYears(callback: CallbackQuery, state: FSMContext):
    await FormState.withYears.set()
