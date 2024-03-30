from twttr import shorten

def test_lower():
    assert shorten("hello") == "hll"

def test_upper():
    assert shorten("AbcdE") == "bcd"

def test_digits():
    assert shorten("12a34b") == "1234b"

def test_consonants():
    assert shorten("HomeWork") == "HmWrk"

def test_punctuation():
    assert shorten("hello!") == "hll!"
