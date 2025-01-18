import random


from typing import Union


from src import try_data


def filter_by_currency(transactions, currency="USD"):
    result = [record for record in transactions if currency in record]
    return result


# print(list(filter_by_currency(try_data.date_for_generators)))


def transaction_descriptions():
    pass


def card_number_generator(start, stop):
    for _ in range(stop - start + 1):
        work_row = []
        for j in range(4):
            card_number_cell = ''.join(str(random.randint(0, 9)) for _ in range(4))
            work_row.append(card_number_cell)
        print(' '.join(work_row))
