from aiogram.types import InlineKeyboardButton

from callback_data_objects import CONFIRM_BUTTON_CALLBACK_OBJECT

# @param callbackType - type for the callback data ( confrim:<callbackType> )
def confirmInlineButton(callbackType: str) -> InlineKeyboardButton:
    return InlineKeyboardButton(
        text = '🆗',
        callback_data = CONFIRM_BUTTON_CALLBACK_OBJECT.new(type = callbackType)
    )
