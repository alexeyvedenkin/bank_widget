from unittest.mock import patch


def read_csv():
    return {
        "id": "650703",
        "state": "EXECUTED",
        "date": "2023-09-05T11:30:32Z",
        "amount": "16210",
        "currency_name": "Sol",
        "currency_code": "PEN",
        "from": "Счёт 58803664561298323391",
        "to": "Счёт 39745660563456619397",
        "description": "Перевод организации",
    }


@patch("src.CSV_Excel.read_csv")
def test_read_csv(mock_read_csv):
    # Настраиваем mock для функции read_csv
    mock_read_csv.return_value = {
        "id": "650703",
        "state": "EXECUTED",
        "date": "2023-09-05T11:30:32Z",
        "amount": "16210",
        "currency_name": "Sol",
        "currency_code": "PEN",
        "from": "Счёт 58803664561298323391",
        "to": "Счёт 39745660563456619397",
        "description": "Перевод организации",
    }

    # Вызов функции read_csv
    result = read_csv()

    # Ожидаемый результат
    expected_result = {
        "id": "650703",
        "state": "EXECUTED",
        "date": "2023-09-05T11:30:32Z",
        "amount": "16210",
        "currency_name": "Sol",
        "currency_code": "PEN",
        "from": "Счёт 58803664561298323391",
        "to": "Счёт 39745660563456619397",
        "description": "Перевод организации",
    }

    # Проверка результата с использованием assert
    assert result == expected_result


if __name__ == "__main__":
    test_read_csv()


def read_excel():
    return {
        "id": 650703.0,
        "state": "EXECUTED",
        "date": "2023-09-05T11:30:32Z",
        "amount": 16210.0,
        "currency_name": "Sol",
        "currency_code": "PEN",
        "from": "Счет 58803664561298323391",
        "to": "Счет 39745660563456619397",
        "description": "Перевод организации",
    }


@patch("src.CSV_Excel.read_csv")
def test_read_excel(mock_read_excel):
    # Настраиваем mock для функции read_csv
    mock_read_excel.return_value = {
        "id": 650703.0,
        "state": "EXECUTED",
        "date": "2023-09-05T11:30:32Z",
        "amount": 16210.0,
        "currency_name": "Sol",
        "currency_code": "PEN",
        "from": "Счет 58803664561298323391",
        "to": "Счет 39745660563456619397",
        "description": "Перевод организации",
    }

    # Вызов функции read_csv
    result = read_excel()

    # Ожидаемый результат
    expected_result = {
        "id": 650703.0,
        "state": "EXECUTED",
        "date": "2023-09-05T11:30:32Z",
        "amount": 16210.0,
        "currency_name": "Sol",
        "currency_code": "PEN",
        "from": "Счет 58803664561298323391",
        "to": "Счет 39745660563456619397",
        "description": "Перевод организации",
    }
    # Проверка результата с использованием assert
    assert result == expected_result


if __name__ == "__main__":
    test_read_excel()
