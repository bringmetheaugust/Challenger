from emoji import emojize, demojize

# @param bool - add or remove emoji
def toggleEmoji(string: str, emoji: str, boolean: bool = True) -> str:
    if boolean:
        return emojize(f'{emoji}{string}', use_aliases = True)
    else:
        return demojize(string, use_aliases = True).replace(emoji, '')

def containEmoji(string: str, emoji) -> bool:
    return emoji in demojize(string, use_aliases = True)
