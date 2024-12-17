from typing import Union


def get_mask_card_number(card_number: Union[int, str]) -> Union[str]:
    """Возвращает маску номера по правилу 'XXXX XX** **** XXXX'
        """
    mcn = str(card_number)
    mask_card_number = mcn[:4] + " " + mcn[4:6] + "** **** " + mcn[-4:]
    return mask_card_number


def get_mask_account(account: Union[int, str]) -> Union[str]:
    """Возвращает маску номера счета по правилу '**XXXX'
        """
    ma = str(account)
    mask_account = "**" + ma[-4:]
    return mask_account
