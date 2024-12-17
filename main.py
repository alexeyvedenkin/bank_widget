from src import masks, widget

print(masks.get_mask_account('12345678901234567890'))
print(masks.get_mask_card_number('1234567890123456'))
print(widget.mask_account_card('Maestro 7000792289606361'))
