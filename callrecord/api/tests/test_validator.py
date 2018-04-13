import pytest

from ..validator import call_data_validator


def test_complete_call_data():
    complete_start_record = {
        "id": "123654789",
        "type": "start",
        "timestamp": "2017-12-12T15:07:13Z",
        "call_id": 71,
        "source": "84912345678",
        "destination": "84917415658"
    }
    assert call_data_validator(complete_start_record) == True

    complete_end_record = {
        "id": "123654789",
        "type": "end",
        "timestamp": "2017-12-12T15:07:13Z",
        "call_id": 71
    }
    assert call_data_validator(complete_end_record) == True


def test_incomplete_call_data():
    complete_start_record = {
        "id": "123654789",
        "type": "start",
        "timestamp": "2017-12-12T15:07:13Z",
        "call_id": 71,
        "source": "84912345678"
    }
    assert call_data_validator(complete_start_record) == False

    complete_end_record = {
        "id": "123654789",
        "type": "end",
        "call_id": 71
    }
    assert call_data_validator(complete_end_record) == False


def test_extra_call_data():
    complete_start_record = {
        "id": "123654789",
        "type": "start",
        "timestamp": "2017-12-12T15:07:13Z",
        "call_id": 71,
        "source": "84912345678",
        "destination": "84917415658",
        "something": "more text here"
    }
    assert call_data_validator(complete_start_record) == False

    complete_end_record = {
        "id": "123654789",
        "type": "end",
        "something": "more text here",
        "timestamp": "2017-12-12T15:07:13Z",
        "call_id": 71
    }
    assert call_data_validator(complete_end_record) == False
