from aiogram.types import CallbackQuery
from aiogram.dispatcher import FSMContext

from bot import dp, bot
from state import FormState, FormItem

@dp.callback_query_handler(state = FormState.withBrands)
async def selectBrand(callback: CallbackQuery, state: FSMContext) -> list:
    currentState = await state.get_data()
    updatedList = updateDataList(currentState['brands'], callback.data)
    await state.update_data(brands = updatedList)

    return updatedList

@dp.callback_query_handler(state = FormState.withYears)
async def selectYears(callback: CallbackQuery, state: FSMContext) -> list:
    currentState = await state.get_data()
    updatedList = updateDataList(currentState['years'], callback.data)
    await state.update_data(years = updatedList)

    return updatedList

def updateDataList(categoryList: list, selectedItem: str) -> list:
    updatedList = list(map(
        lambda item: FormItem(item.data, not item.isSelected) if selectedItem == item.data else item,
        categoryList
    ))

    return updatedList
