from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram import Dispatcher
from aiogram.dispatcher.handler import CancelHandler, current_handler
from aiogram.types import CallbackQuery

class UpdateCatalogueMiddleware(BaseMiddleware):
    def __init__(self):
        super(UpdateCatalogueMiddleware, self).__init__()

    # update catalogueList
    async def on_pre_process_callback_query(self, callback: CallbackQuery, data: dict):
        if ('confirm' in callback.data):
            await callback.answer('😯Seems, You didn\'t choose anything..')
            raise CancelHandler()

        handler = current_handler.get()

        # # Get dispatcher from context
        dispatcher = Dispatcher.get_current()
       
        # raise CancelHandler()

# all middleware types list
# https://github.com/aiogram/aiogram/blob/22094eb477711e644924eaeb2424c8cef20e637a/aiogram/contrib/middlewares/logging.py#L27
