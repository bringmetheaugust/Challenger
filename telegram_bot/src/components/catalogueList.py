from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData
import math

from components.confirmInlineButton import confirmInlineButton, toggleConfirmInlineButton
from constants import CATALOGUE_CHECKBOX_EMOJI, CONFIRM_BUTTON_CALLBACK_QUERY_TYPE, CONFIRM_BUTTON_EMOJI
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
    selectedBrandCount: int = 0
    confirmButton: InlineKeyboardButton = None
    confirmButtonIsSelected: bool = False

    for row in currentBrandList.inline_keyboard:
        for key in row:
            # ignore confirm button
            if CONFIRM_BUTTON_CALLBACK_QUERY_TYPE in key.callback_data:
                if containEmoji(key.text, CONFIRM_BUTTON_EMOJI): confirmButtonIsSelected = True

                confirmButton = key

                continue

            isSelected: bool = containEmoji(key.text, CATALOGUE_CHECKBOX_EMOJI)

            if selectedBrand == key.callback_data:
                if isSelected:
                    key.text = toggleEmoji(key.text, CATALOGUE_CHECKBOX_EMOJI, False)
                else:
                    key.text = toggleEmoji(key.text, CATALOGUE_CHECKBOX_EMOJI)
                    selectedBrandCount += 1
                
                continue

            if isSelected: selectedBrandCount += 1

    if selectedBrandCount > 0 and not confirmButtonIsSelected:
        toggleConfirmInlineButton(confirmButton, True)
    
    if selectedBrandCount == 0 and confirmButtonIsSelected:
        toggleConfirmInlineButton(confirmButton, False)

    return currentBrandList
