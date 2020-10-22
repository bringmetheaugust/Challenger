from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.dispatcher.handler import CancelHandler
from aiogram.types import CallbackQuery

from bot import bot
from state import FormState
from components.catalogueList import catalogueList

class HandlerMiddleware(BaseMiddleware):
    def __init__(self):
        super(HandlerMiddleware, self).__init__()

    # check confirm button
    async def on_pre_process_callback_query(self, callback: CallbackQuery, data: dict):
        if ('confirm' in callback.data):
            state = self.manager.dispatcher.current_state()
            currentState = await state.get_data()

            for category in currentState:
                if (not any(item.isSelected for item in currentState[category])):
                    await callback.answer('😯Seems, You didn\'t choose anything..')
                    raise CancelHandler()

    # update catalogueList
    async def on_post_process_callback_query(self, callback: CallbackQuery, results, data: dict):
        updatedList = results[0]
        
        await bot.edit_message_reply_markup(
            chat_id = callback.from_user.id,
            message_id = callback.message.message_id,
            reply_markup = catalogueList(updatedList)
        )

# all middleware types list
# https://github.com/aiogram/aiogram/blob/22094eb477711e644924eaeb2424c8cef20e637a/aiogram/contrib/middlewares/logging.py
