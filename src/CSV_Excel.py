import csv
import logging
import os
from typing import Any, Dict, List

import pandas as pd


logger = logging.getLogger("CSV_Excel")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler('logs/CSV_Excel.log', "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)

#
#
# excel_data = pd.read_excel("data.transactions_excel.xlsx")
# print(excel_data.shape)
# print(excel_data.head())


def read_csv(filename: str) -> list[Any] | Any:
    """
    Функция принимающая путь к файлу, считывает информацию c CSV файла
    """
    if not os.path.exists(filename):
        logger.error("Файл не найден")
        return []  # В случае ошибки возвращает пустой список
    logger.info("Начало загрузки CSV файла")
    with open(filename, encoding="utf-8") as file:
        reading_csv = csv.DictReader(file, delimiter=";")
        reading = [row for row in reading_csv]
        logger.info("Окончание загрузки CSV файла")
        return reading


# transaction = read_csv("transactions.csv")
#
# print(transaction)


def read_excel(filename: str) -> List[Dict[str, Any]]:
    """
    Function to read Excel file and return its content as a list of dictionaries
    """
    if not os.path.exists(filename):
        logger.error("File not found")
        return []  # Return an empty list in case of error
    logger.info("Начало загрузки Excel файла")
    reading_excel = pd.read_excel(filename)
    # Convert DataFrame to list of dictionaries
    transactions_list = reading_excel.to_dict("records")
    logger.info("Окончание загрузки Excel файла")
    return transactions_list


# operation_excel = read_excel("transactions_excel.xlsx")
# print(operation_excel)
