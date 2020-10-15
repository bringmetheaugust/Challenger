from aiogram.types import InlineKeyboardButton
from utils.emoji import toggleEmoji, containEmoji

from callback_data_objects import CONFIRM_BUTTON_CALLBACK_OBJECT
from constants import CONFIRM_BUTTON_EMOJI, DISABLE_CONFIRM_BUTTON

# @param callbackType - type for the callback data ( confrim:<callbackType> )
def confirmInlineButton(callbackType: str, disabled: bool = True) -> InlineKeyboardButton:
    return InlineKeyboardButton(
        text = toggleEmoji('', DISABLE_CONFIRM_BUTTON if disabled else CONFIRM_BUTTON_EMOJI),
        callback_data = CONFIRM_BUTTON_CALLBACK_OBJECT.new(type = callbackType)
    )

def toggleConfirmInlineButton(button: InlineKeyboardButton, boolean: bool = True) -> InlineKeyboardButton:
    # if disabled
    if containEmoji(button.text, DISABLE_CONFIRM_BUTTON): 
        button.text = toggleEmoji(
            toggleEmoji(button.text, DISABLE_CONFIRM_BUTTON, False),
            CONFIRM_BUTTON_EMOJI
        )
    else:
        button.text = toggleEmoji(
            toggleEmoji(button.text, CONFIRM_BUTTON_EMOJI, False),
            DISABLE_CONFIRM_BUTTON
        )

    return button
