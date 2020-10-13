from aiogram.types import InlineKeyboardButton

def confirmInlineButton(callbackData: str):
    return InlineKeyboardButton(text = 'OK', callback_data = callbackData)
