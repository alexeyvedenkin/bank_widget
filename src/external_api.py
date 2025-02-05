import os
from typing import Any, Dict, List

# noinspection PyPackageRequirements
import requests
# noinspection PyPackageRequirements

from dotenv import load_dotenv

from src.utils import transactions

# Загрузка переменных окружения из .env файла
load_dotenv()

# Получение значения переменной API_KEY из .env-файла
apikey = os.getenv('API_KEY')


def currency_conversion(transaction: dict) -> float:
    """Принимает транзакцию и конвертирует из иностранной валюты в РУБЛИ с запросом на API сайт"""
    if "operationAmount" not in transaction:
        print("Ошибка: ключ 'operationAmount' отсутствует в транзакции")
        return 0.0

    amount = float(transaction["operationAmount"]["amount"])  # получение суммы траты
    currency = transaction["operationAmount"]["currency"]["code"]  # получение валюты

    if currency != "RUB":
        apikey = os.getenv("API_KEY")

        if not apikey:
            print("Ошибка: API ключ не найден. Убедитесь, что он задан в .env файле.")
            return 0.0

        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from{currency}&amount={amount}"

        headers = {"apikey": f"{apikey}"}

        response = requests.get(url, headers=headers)
        response_data = response.json()

        # Отладочная информация
        print(f"Запрос: {url}")
        print(f"Статус ответа: {response.status_code}")
        print(f"Ответ: {response_data}")

        try:
            return round(response_data["result"], 2)
        except KeyError:
            print("Ошибка: ключ 'result' отсутствует в ответе API")
            return 0.0

    return amount


def process_all_transactions(transactions: List[Dict[str, Any]]) -> List[float]:
    """Обрабатывает все транзакции и возвращает список конвертированных сумм в рублях"""
    converted_amounts = []
    for transaction in transactions:
        converted_amount = currency_conversion(transaction)
        converted_amounts.append(converted_amount)
    return converted_amounts


# Пример использования функции с печатью результатов
converted_results = process_all_transactions(transactions)
for result in converted_results:
    print(result)
