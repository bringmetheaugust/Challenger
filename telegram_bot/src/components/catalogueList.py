from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData
import math

from components.confirmInlineButton import confirmInlineButton
from constants import CATALOGUE_CHECKBOX_EMOJI, CONFIRM_BUTTON_CALLBACK_QUERY_TYPE
from utils.emoji import toggleEmoji, containEmoji

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
            if CONFIRM_BUTTON_CALLBACK_QUERY_TYPE in key.callback_data: continue # ignore confirm button

            isSelected: bool = containEmoji(key.text, CATALOGUE_CHECKBOX_EMOJI)

            if selectedBrand == key.callback_data:
                if isSelected:
                    key.text = toggleEmoji(key.text, CATALOGUE_CHECKBOX_EMOJI, False)
                else:
                    key.text = toggleEmoji(key.text, CATALOGUE_CHECKBOX_EMOJI)

    return currentBrandList
