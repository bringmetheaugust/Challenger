from aiogram.utils.callback_data import CallbackData

from constants import CONFIRM_BUTTON_CALLBACK_QUERY_TYPE

CONFIRM_BUTTON_CALLBACK_OBJECT = CallbackData(CONFIRM_BUTTON_CALLBACK_QUERY_TYPE, 'type') # confirm:<type>
