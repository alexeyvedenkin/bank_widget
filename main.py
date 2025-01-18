from src import generators, masks, processing, try_data, widget


for elem in try_data.data_for_masks:
    row = elem.split()
    if len(row[-1]) == 20:
        print(masks.get_mask_account(row[-1]))
print()
for elem in try_data.data_for_masks:
    row = elem.split()
    if len(row[-1]) == 16:
        print(masks.get_mask_card_number(row[-1]))
print()
for elem in try_data.data_for_masks:
    print(widget.mask_account_card(elem))
print()
for elem in try_data.data_for_state_and_date:
    print(widget.get_date(elem['date']))
print()
print(*processing.filter_by_state(try_data.data_for_state_and_date), sep='\n')
print()
print(*processing.sort_by_date(try_data.data_for_state_and_date), sep='\n')
print()
generators.card_number_generator(1, 5)