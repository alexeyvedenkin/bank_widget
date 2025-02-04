from src.utils import get_financial_transactions
import os
print("Current working directory:", os.getcwd())

def test_get_financial_transactions():
    """Тестирует функцию открытия и считывания JSON файла"""
    assert get_financial_transactions("") == []
    assert get_financial_transactions("non_existent_file.json") == []
    assert get_financial_transactions("C:\\Users\\admin\\PycharmProjects\\bank_widget\\data\\operations.json")[0] == {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "31957.58",
            "currency": {
                "name": "руб.",
                "code": "RUB"
                }
            },
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589"
        }

# вызов тестовой функции
test_get_financial_transactions()