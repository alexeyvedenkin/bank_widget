import os
import re
from collections import Counter
from typing import Any

from src import CSV_Excel, generators, processing, utils, widget
from src.widget import get_date, mask_account_card


global sorted_data


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


# def filter_by_currency(transactions: Any, currency_code: Any) -> Any:
#     filtered_transactions = [
#         t for t in transactions
#         if t.get("operationAmount", {}).get("currency", {}).get("code") == currency_code
#         or t.get("currency_code") == currency_code
#     ]
#     print(f"Фильтруем транзакции по валюте: {currency_code}, найдено {len(filtered_transactions)} транзакций")
#     return filtered_transactions


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


# def get_currency(transaction: Any) -> Any:
#     """Определяет валюту транзакции по выбору пользователя
#     """
#     currency_keys = [
#         ["operationAmount", "amount", "code"],
#         ["currency_code"],
#         ["value"],
#         # Добавьте другие ключи здесь, если нужно
#     ]
    # for keys in currency_keys:
    #     value = transaction
    #     try:
    #         for key in keys:
    #             value = value[key]
    #         return value
    #     except KeyError:
    #         continue
    # return "не указана"


def main() -> None:
    """Выполняет взаимодействие с пользователем,
    осуществляет обработку данных в зависимости от выбора пользователя
    """
    try:
        print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
        print("Выберите необходимый пункт меню:")
        print("1. Получить информацию о транзакциях из JSON-файла")
        print("2. Получить информацию о транзакциях из CSV-файла")
        print("3. Получить информацию о транзакциях из XLSX-файла")

        work_file = input("Ваш выбор: ").strip()

        while True:
            if work_file == "1":
                print("Для обработки выбран JSON-файл")
                read_file = utils.get_financial_transactions(os.path.join("data/operations.json"))
                break
            elif work_file == "2":
                print("Для обработки выбран CSV-файл")
                read_file = CSV_Excel.read_csv('transactions.csv')
                break
            elif work_file == "3":
                print("Для обработки выбран XLSX-файл")
                read_file = CSV_Excel.read_excel('transactions_excel.xlsx')
                break
            else:
                work_file = input("Данного варианта нет в списке, попробуйте еще раз:\nВаш выбор: ").strip()
    except ValueError:
        return None

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
            status_operation_filter = processing.filter_by_state(read_file, status_operation)
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
    print(*status_operation_filter[:5], sep='\n')

    while True:
        question_sort_data = input("Отсортировать операции по дате? Да/Нет\nВаш выбор: ").lower()
        if question_sort_data in ["да", "yes"]:
            question_sort_data_reverse = (
                input("Отсортировать по возрастанию или по убыванию?\nВаш выбор: ").strip().lower()
            )
            if question_sort_data_reverse in ["по убыванию", "down"]:
                sorted_data = processing.sort_by_date(status_operation_filter, ascending=True)
                break
            elif question_sort_data_reverse in ["по возрастанию", "up"]:
                sorted_data = processing.sort_by_date(status_operation_filter, ascending=False)
                break
        elif question_sort_data in ["нет", "no"]:
            break
        else:
            print("Данного варианта нет в списке, попробуйте еще раз:")
    print(*sorted_data[:5], sep='\n')
    while True:
        question_currency = input("Выводить транзакции по определенной валюте? Да/Нет\nВаш выбор: ").lower()
        if question_currency in ["да", "yes"]:
            currency_code = input("Введите код валюты (например, RUB, USD): ").upper()
            print(currency_code)
            status_operation_filter = list(generators.filter_by_currency(sorted_data, val_cur=currency_code))
            break
        elif question_currency in ["нет", "no"]:
            break
        else:
            print("Данного варианта нет в списке, попробуйте еще раз:")

    while True:
        question_description = input(
            "Отфильтровать список транзакций по определенному слову в описании? Да/Нет\nВаш выбор: "
        ).lower()
        if question_description in ["да", "yes"]:
            print('''Выберите тип операции из списка:
            Перевод со счета на счет
            Перевод с карты на карту
            Перевод с карты на счет
            Перевод со счета на карту
            Перевод организации
            Открытие вклада
            ''')
            search_string = input("Введите строку поиска: ").strip()
            result_filter = search_transactions_by_description(status_operation_filter, search_string)
            break
        elif question_description in ["нет", "no"]:
            result_filter = status_operation_filter
            break
        else:
            print("Данного варианта нет в списке, попробуйте еще раз:")

    print(f"Распечатываю итоговый список транзакций...\nВсего банковских операций в выборке: {len(result_filter)}\n")
    if result_filter:
        for trans in result_filter:
            amount = float(get_amount(trans))
            currency = currency_code
            # currency = trans.get("operationAmount", {}).get("currency", {}).get("code", {get_currency})
            if "Открытие вклада" in trans["description"]:
                print(
                    f"{get_date(trans['date'])} Открытие вклада\n{widget.mask_account_card(trans['to'])}"
                    f"\nСумма: {amount} {currency}.\n"
                )
            else:
                print(
                    f"{get_date(trans['date'])} {trans['description']}\n{widget.mask_account_card(trans['from'])} -> "
                    f"{mask_account_card(trans['to'])}\nСумма: {amount} {currency}.\n"
                )
    else:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")


if __name__ == "__main__":
    main()


# for elem in try_data.data_for_masks:
#     row = elem.split()
#     if len(row[-1]) == 20:
#         print(masks.get_mask_account(row[-1]))
# print()
# for elem in try_data.data_for_masks:
#     row = elem.split()
#     if len(row[-1]) == 16:
#         print(masks.get_mask_card_number(row[-1]))
# print()
# for elem in try_data.data_for_masks:
#     print(widget.mask_account_card(elem))
# print()
# for elem in try_data.data_for_state_and_date:
#     print(widget.get_date(elem['date']))
# print()
# print(*processing.filter_by_state(try_data.data_for_state_and_date), sep='\n')
# print()
# print(*processing.sort_by_date(try_data.data_for_state_and_date), sep='\n')
# print()
# print(*generators.filter_by_currency(try_data.data_for_generators), sep='\n')
# print()
# for i in range(5):
#     print(list(generators.transaction_descriptions(try_data.data_for_generators)))
# print()
# generators.card_number_generator(1, 5)
# print()
# print(*utils.get_financial_transactions('data/operations.json')[:5], sep='\n')
# print()
# print(type(utils.get_financial_transactions('data/operations.json')))
# transaction = pd.read_csv("transactions.csv")
# print(transaction.head())
# print()
# operation_excel = pd.read_excel("transactions_excel.xlsx")
# print(operation_excel.head())
