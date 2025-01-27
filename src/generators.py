import random


from src import try_data


from src.try_data import *


from typing import Dict, Iterator, List, Union


def filter_by_currency(my_dict, currency="USD"):
    """Функция возвращает итератор, который поочередно выдает транзакции,
    где валюта операции соответствует заданной (например, USD)
    """
    result = []
    for trans in my_dict:
        if trans["operationAmount"]["currency"]["code"] == currency:
            result.append(trans)
    return result


def transaction_descriptions(transactions: list[dict]):
    """Функция возвращает описание каждой операции по очереди
    """
    result = (x.get("description") for x in transactions)  # выводим значение по ключу

    for x in result:
        yield x


def card_number_generator(start, stop):
    for _ in range(stop - start + 1):
        work_row = []
        for j in range(4):
            card_number_cell = ''.join(str(random.randint(0, 9)) for _ in range(4))
            work_row.append(card_number_cell)
        print(' '.join(work_row))
