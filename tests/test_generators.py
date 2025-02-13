import pytest

from typing import Any
from src.generators import (card_number_generator, filter_by_currency, transaction_descriptions, transactions,
                            usd_transactions)


def test_filter_by_currency(filter_by_cur: list[dict]) -> None:
    result = list(filter_by_currency(transactions, "USD"))
    assert result == filter_by_cur


def test_transaction_descriptions(trans_des: list[str]) -> None:
    assert list(transaction_descriptions(usd_transactions)) == trans_des


@pytest.mark.parametrize(
    "transaction, expected",
    [
        ({"description": "Перевод организации"}, "Перевод организации"),
        ({"description": "Перевод со счёта на счёт"}, "Перевод со счёта на счёт"),
        ({"description": "Перевод с карты на карту"}, "Перевод с карты на карту"),
    ],
)


def test_transaction_descriptions_par(transaction: dict[Any, Any], expected: str) -> None:
    descriptions = transaction_descriptions([transaction])
    assert list(descriptions) == [expected]


@pytest.mark.parametrize(
    "start, stop, expected",
    [
        (
            1000000000000000,
            1000000000000003,
            [
                "1000 0000 0000 0000",
                "1000 0000 0000 0001",
                "1000 0000 0000 0002",
                "1000 0000 0000 0003",
            ],
        ),
    ],
)


def test_card_number_generator(start: int, stop: int, expected: str) -> None:
    result = list(card_number_generator(start, stop))
    assert result == expected
