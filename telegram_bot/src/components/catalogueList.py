from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import math
from emoji import emojize, demojize

from components.confirmButton import confirmInlineButton
from constants import CONFIRM_BUTTON_TEXT, CATALOGUE_CHECKBOX_EMOJI

def createCatalogueList(array: list, rowCount: int = 5) -> InlineKeyboardMarkup:
    catalogue = InlineKeyboardMarkup(row_width = rowCount)

    for row in range(0, int(math.ceil(len(array))), rowCount):
        rowList: list = []

        for item in range(0, rowCount):
            try:
                currentItem: str = array[ row + item ]
            except IndexError:
                break

            itemButton = InlineKeyboardButton(text = currentItem, callback_data = currentItem.lower())
            
            rowList.append(itemButton)

        catalogue.row(*rowList)

    catalogue.add(confirmInlineButton('brand'))

    return catalogue

def updateCatalogueList(currentBrandList, selectedBrand) -> InlineKeyboardMarkup:
    for row in currentBrandList.inline_keyboard:
        for key in row:
            if key.text == CONFIRM_BUTTON_TEXT: continue # ignore confirm button

            isSelected: bool = CATALOGUE_CHECKBOX_EMOJI in demojize(key.text)

            if selectedBrand == key.callback_data:
                if isSelected:
                    key.text = demojize(key.text).replace(CATALOGUE_CHECKBOX_EMOJI, '')
                else:
                    key.text = emojize(f'{CATALOGUE_CHECKBOX_EMOJI} {key.text}')

                continue
            
    return currentBrandList
