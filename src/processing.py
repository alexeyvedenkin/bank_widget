from typing import Union


def filter_by_state(work_dicts: Union[list[dict]], state='EXECUTED') -> Union[list[dict]]:
    """Возвращает список словарей, отфильтрованный по полю 'state'
    """
    result = []
    for subject in work_dicts:
        if subject.get('state') == state:
            result.append(subject)
    return result


def sort_by_date(work_dicts: Union[list[dict]], ascending=True) -> Union[list[dict]]:
    """Возвращает список словарей, упорядоченный по дате
    в порядке убывания
    """
    result = sorted(work_dicts, key=lambda date: date.get('date'), reverse=ascending)
    return result
