import pytest


@pytest.fixture
def test_for_masks() -> list[str]:
    """
    Тестовые данные для применения маски счета
    """
    return [
        'Maestro 1596837868705199',
        'Счет 64686473678894779589',
        'MasterCard 7158300734726758',
        'Счет 35383033474447895560',
        'Visa Classic 6831982476737658',
        'Visa Platinum 8990922113665229',
        'Visa Gold 5999414228426353',
        'Счет 73654108430135874305]'
    ]


@pytest.fixture
def test_for_state_and_date() -> list[dict]:
    """
    Тестовые данные для списка словарей
    """
    return [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
    ]


@pytest.fixture
def filter_by_cur() -> list[dict]:
    return [
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572',
         'operationAmount': {'amount': '9824.07', 'currency': {'name': 'USD', 'code': 'USD'}},
         'description': 'Перевод организации', 'from': 'Счет 75106830613657916952', 'to': 'Счет 11776614605963066702'},
        {'id': 142264268, 'state': 'EXECUTED', 'date': '2019-04-04T23:20:05.206878',
         'operationAmount': {'amount': '79114.93', 'currency': {'name': 'USD', 'code': 'USD'}},
         'description': 'Перевод со счета на счет', 'from': 'Счет 19708645243227258542',
         'to': 'Счет 75651667383060284188'},
        {'id': 895315941, 'state': 'EXECUTED', 'date': '2018-08-19T04:27:37.904916',
         'operationAmount': {'amount': '56883.54', 'currency': {'name': 'USD', 'code': 'USD'}},
         'description': 'Перевод с карты на карту', 'from': 'Visa Classic 6831982476737658',
         'to': 'Visa Platinum 8990922113665229'}
    ]


@pytest.fixture
def trans_des() -> list[str]:
    return ['Перевод организации', 'Перевод со счета на счет', 'Перевод с карты на карту']
