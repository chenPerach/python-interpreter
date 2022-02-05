
from sys import exec_prefix


INTEGER, PLUS, MINUS, EOF = 'INTEGER', 'PLUS', 'MINUS', 'EOF'


class Token:
    def __init__(self, type, value) -> None:
        self.type = type
        self.value = value

    def __str__(self):
        return f"Token({self.type},{self.value})"


class Interpeter:
    def __init__(self, text: str) -> None:
        self.text: str = text
        self.pos = 0
        self.current_token: Token = None

    def error(self):
        raise Exception("Error parsing input")

    def parse_integer(self):
        """
        parse integer number that appers in text
        """
        number = ""
        while self.pos < len(self.text) and self.text[self.pos].isdigit():
            number += self.text[self.pos]
            self.pos += 1
        return number
    
    def skip_white_space(self):
        while self.pos < len(self.text) and self.text[self.pos].isspace():
            self.pos += 1

    def get_next_token(self):
        """
        returns the next token in the text
        """
        text = self.text

        self.skip_white_space()

        if self.pos > len(text)-1:
            self.pos += 1
            return Token(EOF, None)

        if text[self.pos].isdigit():
            number = self.parse_integer()
            t = Token(INTEGER, int(number))
            return t

        if text[self.pos] == '-':
            self.pos += 1
            return Token(MINUS, '-')

        if text[self.pos] == '+':
            self.pos += 1
            return Token(PLUS, '+')

        self.error()

    def eat(self, token_type):
        if self.current_token.type == token_type:
            self.current_token = self.get_next_token()
        else:
            self.error()

    def expr(self):

        self.current_token = self.get_next_token()

        left = self.current_token
        self.eat(INTEGER)

        op = self.current_token
        if op.type == PLUS:
            self.eat(PLUS)
        else:
            self.eat(MINUS)

        right = self.current_token
        self.eat(INTEGER)
        if op.type == PLUS:
            return left.value + right.value

        if op.type == MINUS:
            return left.value - right.value


def test_spaces():
    assert Interpeter('5 +   4').expr() == 9
    assert Interpeter('5 +4 ').expr() == 9
    assert Interpeter(' 5+ 4 ').expr() == 9


def test_long_numbers():
    assert Interpeter('55 + 4').expr() == 59


def test_minus():
    assert Interpeter('55 - 4').expr() == 51


def main():
    while True:
        try:
            text = input(">>>")
        except EOFError:
            break
        if text == 'q':
            break
        if not text:
            continue
        interpeter = Interpeter(text)
        res = interpeter.expr()
        print(res)


if __name__ == "__main__":
    main()
