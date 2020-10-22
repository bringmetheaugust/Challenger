from aiogram.types import CallbackQuery, Message, ParseMode
from aiogram.dispatcher import FSMContext

from bot import dp, bot
from state import FormState
from components.catalogueList import updateStateDataList
from utils.validateYear import validateYear

@dp.callback_query_handler(state = FormState.withBrands)
async def selectBrand(callback: CallbackQuery, state: FSMContext) -> list:
    currentState = await state.get_data()
    updatedList = updateStateDataList(currentState['brands'], callback.data)
    await state.update_data(brands = updatedList)

    return updatedList

@dp.message_handler(state = FormState.withYears)
async def selectYears(message: Message, state: FSMContext):
    messageText = message.text

    validateResult = validateYear(messageText)

    if bool(validateResult):
        await state.update_data(years = validateResult)
        await message.answer('cool')
    else:
        await message.answer(
            text ='🤕Seems, You have typed invalid year\'s data.\n🧐Correct format is single year (<b>2007</b> e.g) or range (<b>2001-2007</b> e.g)',
            parse_mode = ParseMode.HTML
        )
