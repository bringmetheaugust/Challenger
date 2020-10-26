from aiogram.types import CallbackQuery, Message, ParseMode
from aiogram.dispatcher import FSMContext

from bot import dp, bot
from state import FormState
from components.catalogueList import updateStateDataList
from utils.validateYear import validateYear
from constants import CONFIRM_BUTTON_CALLBACK_QUERY_TYPE

# confirm button filters
noConfirmButton = lambda callback: not CONFIRM_BUTTON_CALLBACK_QUERY_TYPE in callback.data
isConfirmButton = lambda callback: CONFIRM_BUTTON_CALLBACK_QUERY_TYPE in callback.data

@dp.callback_query_handler(noConfirmButton, state = FormState.withBrands)
async def selectBrand(callback: CallbackQuery, state: FSMContext) -> list:
    currentState = await state.get_data()
    updatedList = updateStateDataList(currentState['brands'], callback.data)
    await state.update_data(brands = updatedList)

    return updatedList

@dp.callback_query_handler(isConfirmButton, state = FormState.withBrands)
async def confirmBrand(callback: CallbackQuery, state: FSMContext) -> list:
    await FormState.withYears.set()
    await callback.bot.send_message(
        text = 'Great!🚐\nType 1st registration year (single <b>2007</b> or range <b>2001-2009</b> e.g).',
        chat_id = callback.message.chat.id,
        parse_mode = ParseMode.HTML
    )

    return None # cancel post middleware


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
