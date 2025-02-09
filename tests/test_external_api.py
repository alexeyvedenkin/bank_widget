from unittest.mock import patch

import os, pytest

from src.external_api import currency_conversion, process_all_transactions

transaction = {
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {
        "amount": "8000",
        "currency": {
            "name": "USD",
            "code": "USD"
        }}}

test_lst = [
    {
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {
            "amount": "8000.0",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        }
    },
    {
        "id": 41428830,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {
            "amount": "5000.0",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        }
    },
]


@patch("requests.get")
def test_currency_conversion(mock_get):
    mock_get.return_value.status_code = 100
    mock_get.return_value.json.return_value = {'success': True, 'timestamp': 1720199764, 'base': 'USD',
                                               'date': '2024-07-05',
                                               'rates': {'RUB': 100}, 'result': 800000.0}
    assert currency_conversion(transaction) == 800000.0

wrong_api = '123'

def test_currency_conversion_not_apikey():
    if wrong_api != os.getenv("API_KEY") or not os.getenv("API_KEY"):
        pytest.raises(AssertionError, match="Ошибка: API ключ не найден. Убедитесь, что он задан в .env файле.")


# def test_process_all_transactions():
#     assert type(process_all_transactions(test_lst)) == list[float]
#
#
# print(process_all_transactions(currency_conversion(test_lst)))
