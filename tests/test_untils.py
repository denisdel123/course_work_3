import json
import pytest
from untils import untils


def test_get_operation():
    assert untils.get_operation('data/operations.json') == list


def test_operation_executed():
    assert untils.operation_executed() == list


def test_check_time():
    assert untils.check_time() == list
