from aiogram.dispatcher.filters.state import State, StatesGroup

class FormState(StatesGroup):
    withBrands = State()
    withYears = State()
    withPrice = State()

# inline keyboard item
class FormItem:
    def __init__(self, itemData: str, isSelected = False):
        self.data: str = itemData
        self.isSelected: bool = isSelected
