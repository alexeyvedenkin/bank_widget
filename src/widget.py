from typing import Union

from src import masks


def mask_account_card(full_row: Union[str]) -> Union[str]:
    """Возвращает строку по маске для счета или карты
    """
    work_row = full_row.split()
    if work_row[0] in ['счет', 'расчетный', 'account']:
        mask = masks.get_mask_card_number(work_row[-1])
        work_row[-1] = mask
        result = ' '.join(work_row)
    else:
        mask = masks.get_mask_account(work_row[-1])
        work_row[-1] = mask
        result = ' '.join(work_row)
    return result


def get_date(full_date: Union[str]) -> Union[str]:
    """Возвращает дату в формате ДД.ММ.ГГГГ
    """
    work_date = full_date[:10].split('-')
    normal_date = '.'.join(reversed(work_date))

    return normal_date
