import random


from src import try_data


# from typing import Union


def filter_by_currency(transactions: list[dict], currency="USD"):
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency:
            yield transaction

# print(list(filter_by_currency(try_data.date_for_generators, 'USD')))


usd_transactions = list(filter_by_currency((try_data.date_for_generators), "USD"))
for transact in usd_transactions:
    print(transact)


def transaction_descriptions(transactions: list[dict]):
    """Функция возвращает описание каждой операции по очереди
    """
    result = (x.get("description") for x in transactions)  # выводим значение по ключу

    for x in result:
        yield x
descriptions = list(transaction_descriptions(usd_transactions))
print(*list(descriptions), sep="\n")


print(transaction_descriptions(try_data.date_for_generators))


def card_number_generator(start, stop):
    for _ in range(stop - start + 1):
        work_row = []
        for j in range(4):
            card_number_cell = ''.join(str(random.randint(0, 9)) for _ in range(4))
            work_row.append(card_number_cell)
        print(' '.join(work_row))
