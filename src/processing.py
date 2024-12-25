from typing import Union


def filter_by_state(work_dict: Union[list[dict]]) -> Union[list[dict]]:
    """Что-то возвращает
    """
    result = []
    for subject in work_dict:
        if subject.get('state') == 'EXECUTED':
            result.append(subject)

    return result
    





