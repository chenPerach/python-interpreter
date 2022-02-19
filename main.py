
from ast import Mult
from sys import exec_prefix


INTEGER, PLUS, MINUS, MUL, DIV, EOF = 'INTEGER', 'PLUS', 'MINUS', 'MUL', 'DIV', 'EOF'
OPS = {
    PLUS: lambda x, y: x+y,
    MINUS: lambda x, y: x-y,
    MUL: lambda x, y: x*y,
    DIV: lambda x, y: x//y,
}


class Token:
    def __init__(self, type, value) -> None:
        self.type = type
        self.value = value

    def __str__(self):
        return f"Token({self.type},{self.value})"


class Interpreter:
    def __init__(self, text: str) -> None:
        self.text: str = text
        self.pos = 0
        self.current_token: Token = self.get_next_token()

    def error(self):
        raise Exception("Invalid Syntax")

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

        if text[self.pos] == '*':
            self.pos += 1
            return Token(MUL, '*')

        if text[self.pos] == '/':
            self.pos += 1
            return Token(DIV, '/')

        self.error()

    def eat(self, token_type):
        if self.current_token.type == token_type:
            self.current_token = self.get_next_token()
        else:
            self.error()
    def factor(self):
        token = self.current_token
        self.eat(INTEGER)
        return token
    def div_mul(self):
        result = self.factor()

        while self.current_token.type in (MUL,DIV):
            op = self.current_token
            self.eat(op.type)
            right = self.factor()

            result = Token(INTEGER, OPS[op.type](result.value, right.value))
        return result
        
    def expr(self):
        # self.current_token = self.get_next_token()
        result = self.div_mul()

        while self.current_token.type in (PLUS,MINUS):
            op = self.current_token
            self.eat(op.type)
            right = self.div_mul()

            result = Token(INTEGER, OPS[op.type](result.value, right.value))
        
        return result.value


def test_spaces():
    assert Interpreter('5 +   4').expr() == 9
    assert Interpreter('5 +4 ').expr() == 9
    assert Interpreter(' 5+ 4 ').expr() == 9


def test_long_numbers():
    assert Interpreter('55 + 4').expr() == 59


def test_arithmatics():
    assert Interpreter('55 + 4').expr() == 59
    assert Interpreter('55 - 4').expr() == 51
    assert Interpreter('55 * 4').expr() == 220
    assert Interpreter('40 / 4').expr() == 10


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
