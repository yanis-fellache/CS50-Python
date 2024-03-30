from fuel import convert, gauge
import pytest

def test_E():
    assert gauge(convert("0/1")) == "E"
    assert gauge(convert("1/100")) == "E"

def test_F():
    assert gauge(convert("4/4")) == "F"
    assert gauge(convert("99/100")) == "F"

def test_percentage():
    assert gauge(convert("1/2")) == "50%"
    assert gauge(convert("1/4")) == "25%"

def test_errors():
    with pytest.raises(ValueError):
        gauge(convert("1/a"))

    with pytest.raises(ZeroDivisionError):
        gauge(convert("0/0"))


