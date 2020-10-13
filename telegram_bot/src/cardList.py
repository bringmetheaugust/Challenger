from aiogram.types import \
    Message, CallbackQuery, InlineKeyboardButton, \
    InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
from emoji import emojize, demojize

from confirmButton import confirmInlineButton

carList: list = ['BMW', 'Ford', 'Audi', 'Dodge']
checkboxEmoji: str = ':ballot_box_with_check:'

def createBrandList() -> InlineKeyboardMarkup:
    carBrandMenu = InlineKeyboardMarkup(row_width = 3)

    for brand in carList:
        brandButton = InlineKeyboardButton(text = brand, callback_data = brand)
        carBrandMenu.row(brandButton)

    return carBrandMenu

def updateBrandList(currentBrandList, selectedBrand) -> InlineKeyboardMarkup:
    selectedBrandCount: int = 0

    for row in currentBrandList.inline_keyboard:
        for key in row:
            if key.text == 'OK': continue # ignore confirm button

            isSelected: bool = checkboxEmoji in demojize(key.text)

            if selectedBrand == key.callback_data:
                if isSelected:
                    key.text = demojize(key.text).replace(checkboxEmoji, '')
                else:
                    key.text = emojize(f'{checkboxEmoji} {key.text}')
                    selectedBrandCount += 1

                continue

            if isSelected: selectedBrandCount += 1

    if bool(selectedBrandCount):
        if (not currentBrandList.inline_keyboard[-1][0].text == 'OK'):
            currentBrandList.add(confirmInlineButton('brand'))
    else:
        currentBrandList.inline_keyboard.pop()
            
    return currentBrandList
