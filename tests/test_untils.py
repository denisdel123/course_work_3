import pytest

from utils.utils_2 import change_format_output, add_in_list_date, sort_json_operations, change_format_date


def test_change_format_output():
    tes = {
        "date": "20.07.2015",
        "amount": "31957.58",
        "name": "руб.",
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589"
    }

    assert change_format_output(tes) == '20.07.2015 Перевод организации\n' \
                                        'Maestro 1596 15** **** 5199 -> **6468\n' \
                                        '31957.58 руб.\n'


def test_add_in_list_date():
    tes = {'date': '26. 08. 2019', 'amount': '31957.58', 'name': 'руб.', 'description': 'Перевод организации',
           'from': 'Maestro 1596837868705199', 'to': 'Счет 64686473678894779589'}, \
        {'date': '03. 07. 2019', 'amount': '8221.37', 'name': 'USD', 'description': 'Перевод организации',
         'from': 'MasterCard 7158300734726758', 'to': 'Счет 35383033474447895560'}, \
        {'date': '30. 06. 2018', 'amount': '9824.07', 'name': 'USD', 'description': 'Перевод организации',
         'from': 'Счет 75106830613657916952', 'to': 'Счет 11776614605963066702'}, \
        {'date': '04. 04. 2019', 'amount': '79114.93', 'name': 'USD', 'description': 'Перевод со счета на счет',
         'from': 'Счет 19708645243227258542', 'to': 'Счет 75651667383060284188'}, \
        {'date': '23. 03. 2019', 'amount': '43318.34', 'name': 'руб.', 'description': 'Перевод со счета на счет',
         'from': 'Счет 44812258784861134719', 'to': 'Счет 74489636417521191160'}

    assert add_in_list_date(tes) == ['26. 08. 2019', '03. 07. 2019', '30. 06. 2018', '04. 04. 2019', '23. 03. 2019']


def test_sort_json_operations():
    tes = ['26. 08. 2019', '03. 07. 2019', '30. 06. 2018', '04. 04. 2019', '23. 03. 2019']

    assert sort_json_operations(tes) == ['30. 06. 2018', '26. 08. 2019', '23. 03. 2019', '04. 04. 2019', '03. 07. 2019']


def test_change_format_date():
    tes = {'id': 441945886, 'state': 'EXECUTED', 'date': '2019-08-26T10:50:58.294041',
           'operationAmount': {'amount': '31957.58', 'currency': {'name': 'руб.', 'code': 'RUB'}},
           'description': 'Перевод организации', 'from': 'Maestro 1596837868705199', 'to': 'Счет 64686473678894779589'}

    assert change_format_date(tes) == {'date': '26. 08. 2019',
                                       'description': 'Перевод организации',
                                       'from': 'Maestro 1596837868705199',
                                       'id': 441945886,
                                       'operationAmount': {'amount': '31957.58',
                                                           'currency': {'code': 'RUB', 'name': 'руб.'}},
                                       'state': 'EXECUTED',
                                       'to': 'Счет 64686473678894779589'}
