from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram import Dispatcher
from aiogram.dispatcher.handler import CancelHandler, current_handler
from aiogram.types import CallbackQuery
from aiogram.dispatcher import FSMContext

from bot import bot
from state import FormState, FormItem
from components.catalogueList import catalogueList

class UpdateCatalogueMiddleware(BaseMiddleware):
    def __init__(self):
        super(UpdateCatalogueMiddleware, self).__init__()

    # update catalogueList
    async def on_pre_process_callback_query(self, callback: CallbackQuery, data: dict):
        if ('confirm' in callback.data):
            await callback.answer('😯Seems, You didn\'t choose anything..')
            raise CancelHandler()

        state = self.manager.dispatcher.current_state()
        currentState = await state.get_data()
        selectedItem = callback.data

        updatedList: list = None

        if (FormState.withBrands):
            updatedList = updateCatalogueList(currentState['brands'], selectedItem)
            await state.update_data(brands = updatedList)
        elif (FormState.withPrice):
            updatedList = updateCatalogueList(currentState['years'], selectedItem)
            await state.update_data(years = updatedList)

        await bot.edit_message_reply_markup(
            chat_id = callback.from_user.id,
            message_id = callback.message.message_id,
            reply_markup = catalogueList(updatedList)
        )

def updateCatalogueList(categoryList: list, selectedItem: str) -> list:
    updatedList = list(map(
        lambda item: FormItem(item.data, not item.isSelected) if selectedItem == item.data else item,
        categoryList
    ))

    return updatedList

# all middleware types list
# https://github.com/aiogram/aiogram/blob/22094eb477711e644924eaeb2424c8cef20e637a/aiogram/contrib/middlewares/logging.py#L27
