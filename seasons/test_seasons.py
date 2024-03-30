from seasons import convert
import pytest

def test_correct():
    assert convert("2007-07-24") == "Eight million, six hundred thirty-two thousand, eight hundred minutes"
    assert convert("2022-12-22") == "Five hundred twenty-five thousand, six hundred minutes"

def test_incorrect():
    with pytest.raises(ValueError):
        convert("January 1, 1999")
