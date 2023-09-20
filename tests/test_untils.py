

import pytest

from untils import untils, main


def test_get_operation():
    assert untils.get_operation('data/operations.json') != list


def test_operation_executed():
    assert untils.operation_executed([{
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "31957.58",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589"
    }]) != list


def test_check_time():
    with pytest.raises(AssertionError):
        assert untils.check_time([{
            "id": 441945886,
            "state": "EXECUTED",
            "date": "13, 07, 2019, 18, 51, 29".split(', '),
            "operationAmount": {
                "amount": "31957.58",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589"
        }]) == list


def test_enter_info():
    with pytest.raises(IndexError):
        time = [['26', '08', '2019', '10', '50', '58'], ['26', '08', '2019', '10', '50', '58'],
                ['26', '08', '2019', '10', '50', '58'], ['26', '08', '2019', '10', '50', '58']]
        oper = [{
            "id": 441945886,
            "state": "EXECUTED",
            "date": "13, 07, 2019, 18, 51, 29".split(', '),
            "operationAmount": {
                "amount": "31957.58",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589"
        }]
        assert untils.enter_info(time, oper) == list

def test_print_info():
    with pytest.raises(AssertionError):
        result = [{
            "id": 441945886,
            "state": "EXECUTED",
            "date": "13, 07, 2019, 18, 51, 29".split(', '),
            "operationAmount": {
                "amount": "31957.58",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589"
        }]
        assert untils.print_info(result) == list




