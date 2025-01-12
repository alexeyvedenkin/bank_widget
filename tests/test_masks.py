import pytest


from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number():
    assert get_mask_card_number("1234567890123456") == "1234 56** **** 3456"
    assert get_mask_card_number(1234567890123456) == "1234 56** **** 3456"


# def test_get_mask_card_number_type_error(test_for_masks):
#     with pytest.raises(TypeError) as exc_info:
#         exc_info = not int(test_for_masks)
#
#
# def test_get_mask_card_number_length_error(test_for_masks):
#     with pytest.raises(ValueError) as exc_info:
#         len(test_for_masks) != 16


def test_get_mask_account():
    assert get_mask_account("12345678901234567890") == "**7890"
    assert get_mask_account(12345678901234567890) == "**7890"


# def test_get_mask_account_type_error(test_for_masks):
#     with pytest.raises(TypeError) as exc_info:
#         not int(test_for_masks)
#
#
# def test_get_mask_account_length_error(test_for_masks):
#     with pytest.raises(ValueError) as exc_info:
#         len(test_for_masks) != 20
