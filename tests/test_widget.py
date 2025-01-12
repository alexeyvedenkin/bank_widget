import pytest

from src.widget import mask_account_card, get_date


def test_mask_account_card():
    assert mask_account_card('Maestro 1596837868705199') == 'Maestro 1596 83** **** 5199'
    assert mask_account_card('Счет 64686473678894779589') == 'Счет **9589'


def test_mask_account_card_value_error():
    with pytest.raises(ValueError):
        mask_account_card('1111111111')


# def test_mask_account_card_type_error():
#     with pytest.raises(TypeError):
#         mask_account_card('')


def test_get_date():
    assert get_date('2019-07-03T18:35:29.512364') == '03.07.2019'


def test_get_date_type_error():
    with pytest.raises(TypeError):
        get_date('1111111111')
