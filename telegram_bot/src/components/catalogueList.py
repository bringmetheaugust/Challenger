from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData
import math

from components.confirmInlineButton import confirmInlineButton
from state import FormItem

# @param array - list of FormItem
# @param rowCount - count of items in one row
def catalogueList(array: list, confirmButtonCallbackType: str, rowCount: int = 5) -> InlineKeyboardMarkup:
    catalogue = InlineKeyboardMarkup(row_width = rowCount)

    for row in range(0, int(math.ceil(len(array))), rowCount):
        rowList: list = []

        for item in range(0, rowCount):
            try:
                currentItem: FormItem = array[ row + item ]
            except IndexError:
                break

            itemText = currentItem.data['title']

            itemButton = InlineKeyboardButton(
                text = f'☑️{itemText}' if currentItem.isSelected else itemText,
                callback_data = currentItem.data['id']
            )
            
            rowList.append(itemButton)

        catalogue.row(*rowList)

    catalogue.add(confirmInlineButton(confirmButtonCallbackType))

    return catalogue

def updateStateDataList(categoryList: list, selectedItem: str) -> list:
    updatedList = list(map(
        lambda item: FormItem(item.data, not item.isSelected) if selectedItem == str(item.data['id']) else item,
        categoryList
    ))

    return updatedList
