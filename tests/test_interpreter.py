from src.interpreter import *
def test_spaces():
    assert Interpreter('5 +   4').expr() == 9
    assert Interpreter('5 +4 ').expr() == 9
    assert Interpreter(' 5+ 4 ').expr() == 9

def test_add():
    assert Interpreter('5+4').expr() == 9
    assert Interpreter('5+6').expr() == 11
    assert Interpreter('2+6').expr() == 8
    assert Interpreter('0+6').expr() == 6
    
def test_sub():
    assert Interpreter('5-0').expr() == 1
    assert Interpreter('5-6').expr() == -1
    assert Interpreter('2-6').expr() == -4
    assert Interpreter('0-6').expr() == -6
    

def test_long_numbers():
    assert Interpreter('55 + 53426').expr() == 53481
    assert Interpreter('53426+55').expr() == 53481


def test_arithmatics():
    assert Interpreter('40 / 4').expr() == 10
    assert Interpreter('40 / 4+  55 * 4-55 - 4').expr() == 10+220-59
    assert Interpreter('30 * 1 - 55 * 0').expr() == 30


