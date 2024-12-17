from typing import Union
from src.masks import *

def mask_account_card(official_row: Union[str]) -> Union[str]:
    """Возвращает строку по маске для счета или карты
    """
    if official_row[-17] == " ":
        result = official_row.replace(official_row[-16:], get_mask_card_number(official_row[-16]))
    else:
        result = official_row.replace(official_row[-20:], get_mask_account(official_row[-20]))
    return result
