import pytest

from src import try_data
from src.generators import filter_by_currency, transaction_descriptions

# # from src.generators import card_number_generator



# from src.try_data import *


def test_filter_by_currency(data_for_generators):
    result = list(filter_by_currency(try_data.data_for_generators, "USD"))
    for i in range(len(result)):
        for j in range(len(try_data.data_for_generators)):
            if result[i] != try_data.data_for_generators[j]:
                if type(result[i]) is not type(try_data.data_for_generators[j]):
                    raise TypeError("Разные типы данных")
                elif type(result) is list[list]:
                    raise TypeError("Задан другой тип данных")

    return result

#
# def test_transaction_descriptions(trans_des):
#     assert list(transaction_descriptions(trans)) == trans_des
#
#
# def test_transaction_descriptions(trans_des):
#     assert list(transaction_descriptions(trans)) == trans_des
#


@pytest.mark.parametrize(
    "transaction, expected",
    [
        ({"description": "Перевод организации"}, "Перевод организации"),
        ({"description": "Перевод со счёта на счёт"}, "Перевод со счёта на счёт"),
        ({"description": "Перевод с карты на карту"}, "Перевод с карты на карту"),
    ],
)
def test_transaction_descriptions_par(transaction: [dict], expected: [str]):
    descriptions = transaction_descriptions([try_data.data_for_generators])
    assert list(descriptions) == [expected]


# @pytest.mark.parametrize(
#     "start, stop, expected",
#     [
#         (
#             1000000000000000,
#             1000000000000003,
#             [
#                 "1000 0000 0000 0000",
#                 "1000 0000 0000 0001",
#                 "1000 0000 0000 0002",
#                 "1000 0000 0000 0003",
#             ],
#         ),
#     ],
# )


# def test_card_number_generator(start, stop):
#     result = card_number_generator(start, stop)
#     assert len(result) == 5


def test_card_number_generator(card_number_generator):
    x = ''.join(card_number_generator.split())
    print(x)
    if not x.isdigit():
        print('Ошибка')
