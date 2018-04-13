import pytest

from ..views import save_call_data


def test_complete_call_data():
    complete_start_record = {
        "id": "123654789",
        "type": "start",
        "timestamp": "2017-12-12T15:07:13Z",
        "call_id": 71,
        "source": "84912345678",
        "destination": "84917415658"
    }
    assert save_call_data(complete_start_record) == (
        {'success': 'POST method is working'}, 200)

    complete_end_record = {
        "id": "123654789",
        "type": "end",
        "timestamp": "2017-12-12T15:07:13Z",
        "call_id": 71
    }
    assert save_call_data(complete_end_record) == (
        {'success': 'POST method is working'}, 200)
