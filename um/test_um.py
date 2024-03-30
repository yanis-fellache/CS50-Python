from um import count

def test_no_um():
    assert count("hello world") == 0
    assert count("yummy") == 0

def test_one_um():
    assert count("Hello, um, world") == 1
    assert count("Um, hello world") == 1

def test_many_um():
    assert count("Um, hello, um, world") == 2
    assert count("Um, um, hello, um, world, um, um") == 5


