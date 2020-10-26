from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.dispatcher.handler import CancelHandler
from aiogram.types import CallbackQuery, ParseMode

from bot import bot
from state import FormState, FormItem
from components.catalogueList import catalogueList
from constants import CONFIRM_BUTTON_CALLBACK_QUERY_TYPE

class HandlerMiddleware(BaseMiddleware):
    def __init__(self):
        super(HandlerMiddleware, self).__init__()

    # check confirm button
    async def on_pre_process_callback_query(self, callback: CallbackQuery, data: dict):
        if (CONFIRM_BUTTON_CALLBACK_QUERY_TYPE in callback.data):
            state = self.manager.dispatcher.current_state()
            currentStateData = await state.get_data()
            
            # check empty category lists
            for category in currentStateData:
                if (not any(item.isSelected for item in currentStateData[category])):
                    await callback.bot.send_message(
                        text = '☹️Seems, You didn\'t choose anything...\n🥺Please, select at least one car brand.',
                        chat_id = callback.message.chat.id,
                        parse_mode = ParseMode.HTML
                    )
                    raise CancelHandler()

    # update catalogueList
    async def on_post_process_callback_query(self, callback: CallbackQuery, results, data: dict):
        if (not bool(results)): return

        updatedList, *_ = results
        
        await bot.edit_message_reply_markup(
            chat_id = callback.from_user.id,
            message_id = callback.message.message_id,
            reply_markup = catalogueList(updatedList)
        )

# all middleware types list
# https://github.com/aiogram/aiogram/blob/22094eb477711e644924eaeb2424c8cef20e637a/aiogram/contrib/middlewares/logging.py
