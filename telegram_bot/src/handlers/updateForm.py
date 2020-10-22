from aiogram.types import CallbackQuery
from aiogram.dispatcher import FSMContext

from bot import dp, bot
from state import FormState
from utils.updateStateDataList import updateStateDataList

@dp.callback_query_handler(state = FormState.withBrands)
async def selectBrand(callback: CallbackQuery, state: FSMContext) -> list:
    currentState = await state.get_data()
    updatedList = updateStateDataList(currentState['brands'], callback.data)
    await state.update_data(brands = updatedList)

    return updatedList

@dp.callback_query_handler(state = FormState.withYears)
async def selectYears(callback: CallbackQuery, state: FSMContext) -> list:
    currentState = await state.get_data()
    updatedList = updateStateDataList(currentState['years'], callback.data)
    await state.update_data(years = updatedList)

    return updatedList
