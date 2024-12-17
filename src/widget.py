from typing import Union
from src import masks


def mask_account_card(full_row: Union[str]) -> Union[str]:
    """Возвращает строку по маске для счета или карты
    """
    if full_row[-17] == " ":
        mask = masks.get_mask_card_number(full_row[-16:])
        result = full_row.replace(full_row[-16:], mask)
    else:
        mask = masks.get_mask_account(full_row[-20:])
        result = full_row.replace(full_row[-20:], mask)
    return result
