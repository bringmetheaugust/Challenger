from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from emoji import emojize, demojize

from components.confirmButton import confirmInlineButton
from constants import CONFIRM_BUTTON_TEXT, CATALOGUE_CHECKBOX_EMOJI


def createCatalogueList(array: list, rowCount = 3) -> InlineKeyboardMarkup:
    catalogue = InlineKeyboardMarkup(row_width = 3)

    while True:
        rowList = list()
        rowCount = 1

        for i in range(1, 3):
            item = array[rowCount * i]

            itemButton = InlineKeyboardButton(text = item, callback_data = item.lower())
            rowList.append(itemButton)

            rowCount += 1

        catalogue.row(rowList)

    # for item in array:
    #     itemButton = InlineKeyboardButton(text = item, callback_data = item.lower())
    #     catalogue.row(itemButton)

    catalogue.add(confirmInlineButton('brand'))

    return catalogue

def updateCatalogueList(currentBrandList, selectedBrand) -> InlineKeyboardMarkup:
    # selectedBrandCount: int = 0

    for row in currentBrandList.inline_keyboard:
        for key in row:
            if key.text == CONFIRM_BUTTON_TEXT: continue # ignore confirm button

            isSelected: bool = CATALOGUE_CHECKBOX_EMOJI in demojize(key.text)

            if selectedBrand == key.callback_data:
                if isSelected:
                    key.text = demojize(key.text).replace(CATALOGUE_CHECKBOX_EMOJI, '')
                else:
                    key.text = emojize(f'{CATALOGUE_CHECKBOX_EMOJI} {key.text}')
                    # selectedBrandCount += 1

                continue

            # if isSelected: selectedBrandCount += 1
            
    return currentBrandList
