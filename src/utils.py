import json
import logging
import os
from typing import Any


logger = logging.getLogger('utils')
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler('logs/utils.log', encoding='utf-8', mode='w')
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_financial_transactions(path: str) -> list[Any]:
    """ Получает данные из внешнего JSON-файла и преобразовывает в объект Python
    """
    if not os.path.exists(path):
        logger.error('Не задан путь к исходным данным')
        return []
    with open(path, encoding="utf-8") as file_json:
        logger.info('Получение данных из исходного файла')
        data_json = json.load(file_json)
        logger.info('Полученные данные преобразованы в объект Python')
        # print(*data_json, end='\n')
    return data_json


transactions = get_financial_transactions('data/operations.json')

logger.debug('Вывод данных')
# for transact in transactions:
#     print(transact, end='\n')
