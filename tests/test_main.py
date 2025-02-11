from unittest.mock import patch, mock_open

from main import get_amount, filter_by_state, read_file_json


# Тест для функции read_file_json
@patch(
    "builtins.open",
    new_callable=mock_open,
    read_data='[{"date": "2020-01-19T16:23:39Z", "description":'
    ' "Открытие вклада", "to": "Счет **4321", "operationAmount":'
    ' {"amount": 40542, "currency": {"code": "RUB"}}, "state": '
    '"EXECUTED"}]',
)
def test_read_file_json(mock_file):
    result = read_file_json("dummy_path")
    assert result == [
        {
            "date": "2020-01-19T16:23:39Z",
            "description": "Открытие вклада",
            "to": "Счет **4321",
            "operationAmount": {"amount": 40542, "currency": {"code": "RUB"}},
            "state": "EXECUTED",
        }
    ]


# Тест для функции filter_by_state
def test_filter_by_state():
    transactions = [{"state": "EXECUTED"}, {"state": "PENDING"}]
    result = filter_by_state(transactions, "EXECUTED")
    assert result == [{"state": "EXECUTED"}]


# Тест для функции get_amount
def test_get_amount():
    transaction = {"operationAmount": {"amount": 40542}}
    result = get_amount(transaction)
    assert result == 40542


if __name__ == "__main__":
    test_read_file_json()
    test_filter_by_state()
    test_get_amount()
