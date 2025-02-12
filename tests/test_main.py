from typing import Any
from unittest.mock import mock_open, patch
import main

from src import CSV_Excel, processing, utils, widget
from main import get_amount, get_currency


# Тест для функции read_file_json
# @patch(
#     "builtins.open",
#     new_callable=mock_open,
#     read_data='[{"date": "2020-01-19T16:23:39Z", "description":'
#     ' "Открытие вклада", "to": "Счет **4321", "operationAmount":'
#     ' {"amount": 40542, "currency": {"code": "RUB"}}, "state": '
#     '"EXECUTED"}]',
# )
# def test_read_file_json(mock_file: Any) -> None:
#     result = read_file_json("dummy_path")
#     assert result == [
#         {
#             "date": "2020-01-19T16:23:39Z",
#             "description": "Открытие вклада",
#             "to": "Счет **4321",
#             "operationAmount": {"amount": 40542, "currency": {"code": "RUB"}},
#             "state": "EXECUTED",
#         }
#     ]


# Тест для функции filter_by_state
# def test_filter_by_state() -> None:
#     transactions = [{"state": "EXECUTED"}, {"state": "PENDING"}]
#     result = filter_by_state(transactions, "EXECUTED")
#     assert result == [{"state": "EXECUTED"}]


# Тест для функции get_amount
def test_get_amount() -> None:
    transaction = {"operationAmount": {"amount": 40542}}
    result = get_amount(transaction)
    assert result == 40542


# Тест для функции get_currency
def test_get_currency() -> None:
    transaction = {"currency_code": {"currency_code": "RUB"}}
    result = get_currency(transaction)
    assert result == {"currency_code": "RUB"}


# Тест для функции main
def try_main() -> Any:
    # user_input = ['2', 'executed', 'yes', 'up', 'yes', 'RUB', 'yes', 'Перевод с карты на карту']
    # main.work_file = user_input[0]
    # main.status_operation = user_input[1]
    # main.question_sort_data = user_input[2]
    # main.question_sort_data_reverse = user_input[3]
    # main.question_currency = user_input[4]
    # main.currency_code = user_input[5]
    # main.question_description = user_input[6]
    # main.search_string = user_input[7]
    return f''' '10.05.2020' 'Перевод с карты на карту' \n
        'Visa 7657 17** **** 6531' -> 'Mastercard 5442 62** **** 8510' \n
        'Сумма: 29722.0 RUB.'
        '''


result = try_main()


@patch("main")
def test_main(mock_main: Any) -> None:
    """Настраиваем Mock для функции main
    """
    user_input = ['2', 'executed', 'yes', 'up', 'yes', 'RUB', 'yes', 'Перевод с карты на карту']
    main.work_file = user_input[0]
    main.status_operation = user_input[1]
    main.question_sort_data = user_input[2]
    main.question_sort_data_reverse = user_input[3]
    main.question_currency = user_input[4]
    main.currency_code = user_input[5]
    main.question_description = user_input[6]
    main.search_string = user_input[7]
    # mock_main.return_value = f'''
    #     '10.05.2020' 'Перевод с карты на карту' \n
    #     'Visa 7657 17** **** 6531' -> 'Mastercard 5442 62** **** 8510' \n
    #     'Сумма: 29722.0 RUB.'
    #     '''

    assert mock_main.return_value == try_main()

    # Ожидаемый результат
    expected_result = {
        # "id": "650703",
        # "state": "EXECUTED",
        # "date": "2023-09-05T11:30:32Z",
        # "amount": "16210",
        # "currency_name": "Sol",
        # "currency_code": "PEN",
        # "from": "Счёт 58803664561298323391",
        # "to": "Счёт 39745660563456619397",
        # "description": "Перевод организации",
    }
    #     08.01.2023 Перевод с карты на карту
    #     American Express 9171 90 ** ** ** 6946 -> Visa 1486 89** **** 2527
    #     Сумма: 34114.0 RUB.
    # 


# if __name__ == "__main__":
    # test_read_file_json()
    # test_filter_by_state()
    # test_get_amount()
