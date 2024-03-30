from numb3rs import validate

def test_too_low():
    assert validate("0.0.0.0") == True
    assert validate("-1.-1.-1.-1") == False

def test_too_high():
    assert validate("255.255.255.255") == True
    assert validate("512.512.512.512") == False
    assert validate("1.2.3.1000") == False
    assert validate("275.3.6.28") == False

def test_others():
    assert validate("cat") == False
    assert validate("0") == False
    assert validate("0.0.0") == False
    assert validate("255.275.275.275") == False
