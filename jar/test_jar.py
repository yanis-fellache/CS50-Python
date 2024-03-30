from jar import Jar
import pytest


def test_init():
    with pytest.raises(ValueError):
        Jar(capacity="hello")
    with pytest.raises(ValueError):
        Jar(capacity=-1) 

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    with pytest.raises(ValueError):
        Jar().deposit(15)


def test_withdraw():
    with pytest.raises(ValueError):
        Jar().withdraw(13)
