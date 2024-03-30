from working import convert
import pytest

def test_morning():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:30 AM to 5 PM") == "09:30 to 17:00"
    assert convert("09:00 AM to 05:30 PM") == "09:00 to 17:30"

def test_afternoon():
    assert convert("11 PM to 3 AM") == "23:00 to 03:00"
    assert convert("2:30 PM to 5:43 PM") == "14:30 to 17:43"

def test_error():
    with pytest.raises(ValueError):
        convert("13 AM to 5 PM")
    with pytest.raises(ValueError):
        convert("9:60 AM to 5 PM")
    with pytest.raises(ValueError):
        convert("9 AM 5 PM")

