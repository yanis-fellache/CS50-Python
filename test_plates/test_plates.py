from plates import is_valid


def test_correct():
    assert is_valid("AA") == True
    assert is_valid("AAA") == True
    assert is_valid("AAAA") == True
    assert is_valid("AAAAA") == True
    assert is_valid("AAAAAA") == True
    assert is_valid("AA2220") == True

def test_req1():
    assert is_valid("A") == False
    assert is_valid("AAAAAAA") == False

def test_req2():
    assert is_valid("A222") == False
    assert is_valid("2222") == False
    assert is_valid("2AAA") == False

def test_req3():
    assert is_valid("AA22AA") == False
    assert is_valid("AA2A22") == False

    assert is_valid("AA02") == False
    #assert is_valid("AAAAA0") == False

def test_req4():
    assert is_valid("AA.222") == False
    assert is_valid(".AA222") == False
    assert is_valid("AA222.") == False


