from aiogram.types import InlineKeyboardButton
from emoji import emojize

from constants import CONFIRM_BUTTON_TEXT

def confirmInlineButton(callbackData: str) -> InlineKeyboardButton:
    return InlineKeyboardButton(
        text = emojize(CONFIRM_BUTTON_TEXT),
        callback_data = callbackData
    )
