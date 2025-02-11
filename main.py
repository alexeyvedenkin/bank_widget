import json
import os
import re
from collections import Counter
from typing import Any

import pandas as pd

from src import generators, masks, processing, try_data, utils, widget
from src.CSV_Excel import read_csv, read_excel
from src.widget import get_date, mask_account_card


def read_file_json(file_path: Any) -> Any:
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


def search_transactions_by_description(transactions: Any, search_string: Any) -> list[Any]:
    """Находит операции по заданной в описании строке
    """
    pattern = re.compile(re.escape(search_string), re.IGNORECASE)
    return [transaction for transaction in transactions if pattern.search(transaction.get("description", ""))]


def count_transactions_by_category(transactions: list) -> dict:
    """Определяет количество операций по заданным категориям
    """
    categories = [transaction["description"] for transaction in transactions]
    return dict(Counter(categories))


def filter_by_state(operations: Any, status: Any) -> list[Any]:
    return [t for t in operations if isinstance(t.get("state", ""), str) and t.get("state", "").upper() == status]


def filter_by_currency(transactions: Any, currency_code: Any) -> Any:
    filtered_transactions = [
        t for t in transactions if t.get("operationAmount", {}).get("currency", {}).get("code") == currency_code
    ]
    print(f"Фильтруем транзакции по валюте: {currency_code}, найдено {len(filtered_transactions)} транзакций")
    return filtered_transactions


def get_amount(transaction: Any) -> Any:
    """Определяет сумму транзакции, независимо от структуры данных
    """
    amount_keys = [
        ["operationAmount", "amount"],
        ["amount"],
        ["value"],
        # Добавьте другие ключи здесь, если нужно
    ]
    for keys in amount_keys:
        value = transaction
        try:
            for key in keys:
                value = value[key]
            return value
        except KeyError:
            continue
    return "не указана"


def main() -> None:
    """Выполняет взаимодействие с пользователем,
    осуществляет обработку данных в зависимости от выбора пользователя
    """
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    work_file = input("Ваш выбор: ").strip()

    while True:
        if work_file == "1":
            print("Для обработки выбран JSON-файл")
            read_file = read_file_json(os.path.join(os.path.dirname(__file__), "data/operations.json"))
            break
        elif work_file == "2":
            print("Для обработки выбран CSV-файл")
            read_file = read_csv("C:\\Users\\Макс\\my_prj\\bank widget\\transactions.csv")
            break
        elif work_file == "3":
            print("Для обработки выбран XLSX-файл")
            read_file = read_excel("C:\\Users\\Макс\\my_prj\\bank widget\\transactions_excel.xlsx")
            break
        else:
            work_file = input("Данного варианта нет в списке, попробуйте еще раз:\nВаш выбор: ").strip()

    status_operation = (
        input(
            "\nВведите статус, по которому необходимо выполнить фильтрацию. "
            "\nДоступные для фильтрации статусы: EXECUTED, CANCELED, PENDING:\nВвод: "
        )
        .strip()
        .upper()
    )

    while True:
        if status_operation in {"EXECUTED", "CANCELED", "PENDING"}:
            status_operation_filter = filter_by_state(read_file, status_operation)
            break
        else:
            status_operation = (
                input(
                    f"Статус {status_operation} не доступен.\n"
                    "\nВведите статус, по которому необходимо выполнить фильтрацию."
                    "\nДоступные для фильтрации статусы: EXECUTED, CANCELED, PENDING:\nВвод: "
                )
                .strip()
                .upper()
            )

    while True:
        question_sort_data = input("Отсортировать операции по дате? Да/Нет\nВаш выбор: ").lower()
        if question_sort_data == "да":
            question_sort_data_reverse = (
                input("Отсортировать по возрастанию или по убыванию?\nВаш выбор: ").strip().lower()
            )
            reverse = question_sort_data_reverse == "по убыванию"
            status_operation_filter.sort(key=lambda t: t.get("date", ""), reverse=reverse)
            break
        elif question_sort_data == "нет":
            break
        else:
            print("Данного варианта нет в списке, попробуйте еще раз:")

    while True:
        question_currency = input("Выводить транзакции по определенной валюте? Да/Нет\nВаш выбор: ").lower()
        if question_currency == "да":
            currency_code = input("Введите код валюты (например, RUB, USD): ").strip().upper()
            status_operation_filter = filter_by_currency(status_operation_filter, currency_code)
            break
        elif question_currency == "нет":
            break
        else:
            print("Данного варианта нет в списке, попробуйте еще раз:")

    while True:
        question_description = input(
            "Отфильтровать список транзакций по определенному слову в описании? Да/Нет\nВаш выбор: "
        ).lower()
        if question_description == "да":
            search_string = input("Введите строку поиска: ").strip()
            result_filter = search_transactions_by_description(status_operation_filter, search_string)
            break
        elif question_description == "нет":
            result_filter = status_operation_filter
            break
        else:
            print("Данного варианта нет в списке, попробуйте еще раз:")

    print(f"Распечатываю итоговый список транзакций...\nВсего банковских операций в выборке: {len(result_filter)}\n")
    if result_filter:
        for trans in result_filter:
            amount = get_amount(trans)
            currency = trans.get("operationAmount", {}).get("currency", {}).get("code", "не указана")
            if "Открытие вклада" in trans["description"]:
                print(
                    f"{get_date(trans['date'])} Открытие вклада\n{mask_account_card(trans['to'])}"
                    f"\nСумма: {amount} {currency}.\n"
                )
            else:
                print(
                    f"{get_date(trans['date'])} {trans['description']}\n{mask_account_card(trans['from'])} -> "
                    f"{mask_account_card(trans['to'])}\nСумма: {amount} {currency}.\n"
                )
    else:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")


if __name__ == "__main__":
    main()


for elem in try_data.data_for_masks:
    row = elem.split()
    if len(row[-1]) == 20:
        print(masks.get_mask_account(row[-1]))
print()
for elem in try_data.data_for_masks:
    row = elem.split()
    if len(row[-1]) == 16:
        print(masks.get_mask_card_number(row[-1]))
print()
for elem in try_data.data_for_masks:
    print(widget.mask_account_card(elem))
print()
for elem in try_data.data_for_state_and_date:
    print(widget.get_date(elem['date']))
print()
print(*processing.filter_by_state(try_data.data_for_state_and_date), sep='\n')
print()
print(*processing.sort_by_date(try_data.data_for_state_and_date), sep='\n')
print()
print(*generators.filter_by_currency(try_data.data_for_generators), sep='\n')
print()
for i in range(5):
    print(list(generators.transaction_descriptions(try_data.data_for_generators)))
print()
generators.card_number_generator(1, 5)
print()
print(*utils.get_financial_transactions('data/operations.json')[:5], sep='\n')
print()
print(type(utils.get_financial_transactions('data/operations.json')))
transaction = pd.read_csv("transactions.csv")
print(transaction.head())
print()
operation_excel = pd.read_excel("transactions_excel.xlsx")
print(operation_excel.head())
