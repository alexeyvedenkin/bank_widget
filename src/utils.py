import json
import os
from typing import Any


def get_financial_transactions(path: str) -> list[Any]:
    """ Получает данные из внешнего JSON-файла и преобразовывает в объект Python
    """
    if not os.path.exists(path):
        return []
    with open(path, encoding="utf-8") as file_json:
        data_json = json.load(file_json)
    return data_json


transactions = get_financial_transactions("C:\\Users\\admin\\PycharmProjects\\bank_widget\\data\\operations.json")

print(transactions, end='\n')
