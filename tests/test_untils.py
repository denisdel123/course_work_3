import pytest

from utils import untils_2, main


def test_change_format_output():
    tes = {
            "date": "20.07.2015",
            "amount": "31957.58",
            "name": "руб.",
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589"
        }
    assert untils_2.change_format_output(tes) == "20.07.2015 Перевод организации Maestro 1596 83** **** 5199 -> Счет **9589 31957.58 руб."
