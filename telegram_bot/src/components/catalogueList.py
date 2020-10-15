from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData
import math
from emoji import emojize, demojize

from components.confirmButton import confirmInlineButton
from constants import CONFIRM_BUTTON_TEXT, CATALOGUE_CHECKBOX_EMOJI

# @param rowCount - count of items in one row
def createCatalogueList(array: list, callbackObject: CallbackData, rowCount: int = 5) -> InlineKeyboardMarkup:
    catalogue = InlineKeyboardMarkup(row_width = rowCount)

    for row in range(0, int(math.ceil(len(array))), rowCount):
        rowList: list = []

        for item in range(0, rowCount):
            try:
                currentItem: str = array[ row + item ]
            except IndexError:
                break

            itemButton = InlineKeyboardButton(
                text = currentItem,
                callback_data = callbackObject.new(data = currentItem.lower())
            )
            
            rowList.append(itemButton)

        catalogue.row(*rowList)

    catalogue.add(confirmInlineButton('brand'))

    return catalogue

# @param currentBrandList - selected InlineKeyboardMarkup
# @param selectedBrand - callback data from selected button
def updateCatalogueList(currentBrandList: InlineKeyboardMarkup, selectedBrand: str) -> InlineKeyboardMarkup:
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
