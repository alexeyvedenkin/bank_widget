from typing import Union

from tests.test_dict import test


def filter_by_state(work_dict: Union[list[dict]]) -> Union[list[dict]]:
    """Возвращает список словарей, отфильтрованный по полю 'state'
    """
    result = []
    for subject in work_dict:
        if subject.get('state') == 'EXECUTED':
            result.append(subject)

    return result


def sort_by_date(work_dict: Union[list[dict]]) -> Union[list[dict]]:
    """Возвращает список словарей, упорядоченный по дате
    в порядке убывания
    """
    result = []
    return result


print(filter_by_state(test))

