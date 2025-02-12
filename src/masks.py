import logging
from typing import Union

# logger = logging.getLogger('masks')
# logger.setLevel(logging.DEBUG)
# file_handler = logging.FileHandler('logs/masks.log', encoding='utf-8', mode='w')
# file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s')
# file_handler.setFormatter(file_formatter)
# logger.addHandler(file_handler)


def get_mask_card_number(card_number: Union[int, str]) -> str:
    """Возвращает маску номера по правилу 'XXXX XX** **** XXXX'
        """
    # logger.debug('Запрос данных для обработки')
    if len(str(card_number)) == 16:
        # logger.debug('Проверяем длину заданной строки')
        mcn = str(card_number)
        if mcn.isdigit():
            # logger.debug('Получаем маску для заданной строки')
            mask_card_number = mcn[:4] + " " + mcn[4:6] + "** **** " + mcn[-4:]
            # logger.debug('Возвращаем маску для дальнейшей работы')
            return mask_card_number
        else:
            # logger.error('Некорректные данные в полученной строке')
            raise TypeError()
    else:
        # logger.error('Некорректная длина полученной строки')
        raise ValueError()


def get_mask_account(account: Union[int, str]) -> Union[str]:
    """Возвращает маску номера счета по правилу '**XXXX'
        """
    # logger.debug('Запрос данных для обработки')
    if len(str(account)) == 20:
        # logger.debug('Проверяем длину заданной строки')
        ma = str(account)
        if ma.isdigit():
            # logger.debug('Получаем маску для заданной строки')
            mask_account = "**" + ma[-4:]
            # logger.debug('Возвращаем маску для дальнейшей работы')
            return mask_account
        else:
            raise TypeError()
    else:
        raise ValueError()
