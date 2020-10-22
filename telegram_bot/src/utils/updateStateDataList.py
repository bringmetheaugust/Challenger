from state import FormItem

def updateStateDataList(categoryList: list, selectedItem: str) -> list:
    updatedList = list(map(
        lambda item: FormItem(item.data, not item.isSelected) if selectedItem == item.data else item,
        categoryList
    ))

    return updatedList
