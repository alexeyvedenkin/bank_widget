from src import masks, processing, widget
from tests.test_data import *


print(masks.get_mask_account('12345678901234567890'))
print()
print(masks.get_mask_card_number('1234567890123456'))
print()
print(widget.mask_account_card('Счет 73654108430135874305'))
print()
print(widget.get_date('2024-03-1198695985929'))
print()
print(*processing.filter_by_state(test), sep='\n')
print()
print(*processing.sort_by_date(test), sep='\n')
