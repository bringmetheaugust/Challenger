from aiogram.types import CallbackQuery, Message, ParseMode
from aiogram.dispatcher import FSMContext

from bot import dp, bot
from state import FormState, FormItem
from components.catalogueList import updateStateDataList, catalogueList
from utils.validateYear import validateYear
from constants import CONFIRM_BUTTON_CALLBACK_QUERY_TYPE, \
    CONFIRM_BUTTON_CALLBACK_BRAND_DATA, CONFIRM_BUTTON_CALLBACK_PRICE_DATA
from utils.fetch import fetch

# confirm button filters
noConfirmButton = lambda callback: not CONFIRM_BUTTON_CALLBACK_QUERY_TYPE in callback.data
isConfirmButton = lambda callback: CONFIRM_BUTTON_CALLBACK_QUERY_TYPE in callback.data

@dp.callback_query_handler(noConfirmButton, state = FormState.withBrands)
async def selectBrand(callback: CallbackQuery, state: FSMContext):
    currentState = await state.get_data()
    updatedList = updateStateDataList(currentState['brands'], callback.data)
    await state.update_data(brands = updatedList)

    return updatedList, CONFIRM_BUTTON_CALLBACK_BRAND_DATA

@dp.callback_query_handler(isConfirmButton, state = FormState.withBrands)
async def confirmBrand(callback: CallbackQuery, state: FSMContext):
    await FormState.withYears.set()
    await callback.bot.send_message(
        text = 'Введiть дату першoї реєстрацiї авто🚐.\nНаприклад, точну <b>2007</b> або перiод <b>2001-2009</b>.',
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
        await FormState.withPrice.set()
        priceList: list = fetch('api/params/price')

        mapedPriceList = list(map(lambda price: FormItem(price), priceList))

        await state.update_data(price = mapedPriceList)
        await message.answer(
            'Оберiть цiновий дiапазон (в долларах <b>США</b>)💵',
            reply_markup = catalogueList(mapedPriceList, CONFIRM_BUTTON_CALLBACK_PRICE_DATA),
            parse_mode = ParseMode.HTML
        )
    else:
        await message.answer(
            text ='Здається, що Ви ввели невiрну дату🤕.\nКорректний формат має бути точний рiк (наприклад, <b>2007</b>) або перiод (<b>2001-2007</b>)🧐',
            parse_mode = ParseMode.HTML
        )

@dp.callback_query_handler(noConfirmButton, state = FormState.withPrice)
async def selectPrice(callback: CallbackQuery, state: FSMContext):
    currentState = await state.get_data()
    updatedList = updateStateDataList(currentState['price'], callback.data)
    await state.update_data(price = updatedList)

    return updatedList, CONFIRM_BUTTON_CALLBACK_PRICE_DATA

@dp.callback_query_handler(isConfirmButton, state = FormState.withPrice)
async def confirmPrice(callback: CallbackQuery, state: FSMContext):
    await FormState.withPrice.set()
    await callback.bot.send_message(
        text = 'ПОКА ШО ВСЁ..',
        chat_id = callback.message.chat.id,
        parse_mode = ParseMode.HTML
    )

    return None # cancel post middleware
