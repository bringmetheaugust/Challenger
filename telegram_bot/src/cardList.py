from aiogram.types import \
    Message, CallbackQuery, InlineKeyboardButton, \
    InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
from emoji import emojize, demojize

carList: list = ['BMW', 'Ford', 'Audi', 'Dodge']
checkboxEmoji: str = ':ballot_box_with_check:'

def createBrandList():
    carBrandMenu = InlineKeyboardMarkup(row_width = 3)

    for brand in carList:
        brandButton = InlineKeyboardButton(text = brand, callback_data = brand)
        carBrandMenu.add(brandButton)

    return carBrandMenu

def updateBrandList(currentBrandList, selectedBrand):
    for row in currentBrandList.inline_keyboard:
        for key in row:
            if selectedBrand == key.callback_data:
                if checkboxEmoji in demojize(key.text):
                    key.text = demojize(key.text).replace(checkboxEmoji, '')
                else:
                    key.text = emojize(f'{checkboxEmoji} {key.text}')
            else:
                continue

    return currentBrandList
