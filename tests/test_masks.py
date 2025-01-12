import pytest


from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number():
    assert get_mask_card_number("1234567890123456") == "1234 56** **** 3456"
    assert get_mask_card_number(1234567890123456) == "1234 56** **** 3456"


def test_get_mask_card_number_type_error():
    with pytest.raises(TypeError):
        get_mask_card_number('abcdefghhgfedcba')


def test_get_mask_card_number_length_error():
    with pytest.raises(ValueError):
        get_mask_card_number('1234566789901234567890')


def test_get_mask_account():
    assert get_mask_account("12345678901234567890") == "**7890"
    assert get_mask_account(12345678901234567890) == "**7890"


def test_get_mask_account_type_error():
    with pytest.raises(TypeError):
        get_mask_account('abcdefghijjihgfedcba')


def test_get_mask_account_length_error(test_for_masks):
    with pytest.raises(ValueError):
        get_mask_account('1234567890123456')
