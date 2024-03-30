import project
import pytest

def test_hangman(monkeypatch):
    simulated_input = "a"
    monkeypatch.setattr('builtins.input', lambda _: simulated_input)

def test_choose_word():
    assert project.choose_word("3") is not None
    assert isinstance(project.choose_word("3"), str)

def test_diplay_word():
    assert project.display_word("able", []) == "____"
    assert project.display_word("able", ["a"]) == "a___"
    assert project.display_word("able", ["b", "e"]) == "_b_e"
    assert project.display_word("able", ["e", "b", "a", "l"]) == "able"

def test_hint():
    assert isinstance(project.hint("hello", ["e", "b", "a", "l"]), str)
    assert len(project.hint("hello", ["e", "b", "a", "l"])) <= 1 == True
    assert project.hint("hello", ["e", "b", "a", "l"]).isalpha() == True

def test_fail():
    assert project.fail(1) == r'''
         -----
         |   |
             |
             |
             |
             |
        ------
        '''
    assert project.fail(2) == r'''
         -----
         |   |
         O   |
             |
             |
             |
        ------
        '''
    assert project.fail(3) == r'''
         -----
         |   |
         O   |
         |   |
             |
             |
        ------
        '''
    assert project.fail(4) == r'''
         -----
         |   |
         O   |
        /|   |
             |
             |
        ------
        '''
    assert project.fail(5) == r'''
         -----
         |   |
         O   |
        /|\  |
             |
             |
        ------
        '''
    assert project.fail(6) == r'''
         -----
         |   |
         O   |
        /|\  |
        /    |
             |
        ------
        '''
    assert project.fail(7) == r'''
         -----
         |   |
         O   |
        /|\  |
        / \  |
             |
        ------
        '''


