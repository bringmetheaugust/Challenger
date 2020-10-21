from aiogram.types import CallbackQuery, InlineKeyboardMarkup
from aiogram.utils import exceptions
from aiogram.dispatcher import FSMContext

from bot import dp, bot
from state import FormState, FormItem
from components.catalogueList import catalogueList

years: list = ['2021', '2020', '2019', '2018', '2017', '2016', '2015', '2014', '2013', '2012', '2011', '2010', '2009', '2008']

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
    await bot.send_message(
        chat_id = update.callback_query.message.chat.id,
        text = '😯Seems, You didn\'t choose anything..'
    )
    
    return True
