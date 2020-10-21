from aiogram.types import CallbackQuery, InlineKeyboardMarkup
from aiogram.utils import exceptions
from aiogram.dispatcher import FSMContext

from bot import dp, bot
from state import FormState, FormItem
from components.catalogueList import catalogueList

@dp.callback_query_handler(state = FormState.withBrands)
async def selectBrand(callback: CallbackQuery, state: FSMContext):
    currentData = await state.get_data()
    currentBrandList: list = currentData['brands']
    selectedBrand = callback.data

    updatedBrandList = list(map(
        lambda brand: FormItem(brand.data, not brand.isSelected) if selectedBrand == brand.data else brand,
        currentBrandList
    ))

    await state.update_data(brands = updatedBrandList)

    await bot.edit_message_reply_markup(
        chat_id = callback.from_user.id,
        message_id = callback.message.message_id,
        reply_markup = catalogueList(updatedBrandList)
    )

@dp.errors_handler(exception = exceptions.MessageNotModified)
async def confirmButton(update, err):
    _, confirmType = update.callback_query.data.split(':')

    if confirmType == 'brand':
        await FormState.withYears.set()
    else:
        await bot.send_message(
            chat_id = update.callback_query.message.chat.id,
            text = '😯Seems, You didn\'t choose anything..'
        )
    
    return True
