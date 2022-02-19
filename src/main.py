from src.interpreter import *

def test_spaces():
    assert Interpreter('5 +   4').expr() == 9
    assert Interpreter('5 +4 ').expr() == 9
    assert Interpreter(' 5+ 4 ').expr() == 9


def test_long_numbers():
    assert Interpreter('55 + 4').expr() == 59


def test_arithmatics():
    assert Interpreter('40 / 4').expr() == 10
    assert Interpreter('40 / 4+  55 * 4-55 - 4').expr() == 10+220-59
    assert Interpreter('30 * 1 - 55 * 0').expr() == 30


def main():
    while True:
        try:
            text = input(">>> ")
        except EOFError:
            break
        if text == 'q':
            break
        if not text:
            continue
        interpeter = Interpreter(text)
        res = interpeter.expr()
        print(res)


if __name__ == "__main__":
    main()
