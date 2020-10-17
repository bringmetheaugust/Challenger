from aiogram.types import InlineKeyboardButton
from utils.emoji import toggleEmoji

from callback_data_objects import CONFIRM_BUTTON_CALLBACK_OBJECT
from constants import CONFIRM_BUTTON_EMOJI

# @param callbackType - type for the callback data ( confrim:<callbackType> )
def confirmInlineButton(callbackType: str) -> InlineKeyboardButton:
    return InlineKeyboardButton(
        text = toggleEmoji('', CONFIRM_BUTTON_EMOJI),
        callback_data = CONFIRM_BUTTON_CALLBACK_OBJECT.new(type = callbackType)
    )

# ! archived function
# def toggleConfirmInlineButton(button: InlineKeyboardButton, boolean: bool = True) -> InlineKeyboardButton:
#     # if disabled
#     if containEmoji(button.text, DISABLE_CONFIRM_BUTTON): 
#         button.text = toggleEmoji(
#             toggleEmoji(button.text, DISABLE_CONFIRM_BUTTON, False),
#             CONFIRM_BUTTON_EMOJI
#         )
#     else:
#         button.text = toggleEmoji(
#             toggleEmoji(button.text, CONFIRM_BUTTON_EMOJI, False),
#             DISABLE_CONFIRM_BUTTON
#         )

#     return button
