import logging


import pandas as pd

from src.CSV_Excel import read_csv, read_excel
from src.utils import get_financial_transactions


def user_input():
    '''Получает от пользователя информацию о типе считываемого файла
    '''
    user_choice = int(input(f'''Привет! Добро пожаловать в программу работы 
        с банковскими транзакциями. 
        Выберите необходимый пункт меню:
        1. Получить информацию о транзакциях из JSON-файла
        2. Получить информацию о транзакциях из CSV-файла
        3. Получить информацию о транзакциях из XLSX-файла :
        '''))


def main():
    pass




