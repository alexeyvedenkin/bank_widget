import json


import logging


import pandas as pd

# from src.CSV_Excel import read_csv, read_excel
from src.utils import get_financial_transactions


from typing import Any

# logger = logging.getLogger("total")
# logger.setLevel(logging.DEBUG)
# file_handler = logging.FileHandler('total.log', "a", encoding="utf-8")
# file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
# file_handler.setFormatter(file_formatter)
# logger.addHandler(file_handler)

def user_input():
    """ Получает от пользователя информацию о типе считываемого файла
    """
    print(f'''Привет! Добро пожаловать в программу работы с банковскими транзакциями. 
    Выберите необходимый пункт меню:
        1. Получить информацию о транзакциях из JSON-файла
        2. Получить информацию о транзакциях из CSV-файла
        3. Получить информацию о транзакциях из XLSX-файла
        ''')
    user_choice = int(input())
    correct_answer = {1: 'JSON-файл', 2: 'CSV-файл', 3: 'XLSX-файл'}
    try:
        if user_choice in correct_answer.keys():
            print(f'Для обработки выбран {correct_answer[user_choice]}')
            return user_choice
        else:
            print(f'Ошибка! Введите корректное значение')

    except ValueError:
        return []


choice = user_input()

# @user_input():
def read_file(user_input: Any):
    try:
        if choice == 1:
            transaction = pd.json_normalize(get_financial_transactions('data/operations.json'))
            # print(transaction[0])
            return transaction
        elif choice == 2:
            transaction = pd.read_csv("transactions.csv")
            # print(transaction.head(3))
            return transaction
        elif choice == 3:
            transaction = pd.read_excel("transactions_excel.xlsx")
            # print(transaction.head(3))
            return transaction

    except ValueError:
        return []


print(read_file(user_input).head(3))
# print(type(read_file(user_input)))

def main():
    pass


if __name__ == "__main__":
    # answer = user_input()
    # print(answer)
    read_file(choice)
    # print(read_file[:3])
