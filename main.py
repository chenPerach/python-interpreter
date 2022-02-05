
from sys import exec_prefix


INTEGER, PLUS, MINUS,MUL,DIV, EOF = 'INTEGER', 'PLUS', 'MINUS','MUL','DIV', 'EOF'
OPS = {
    PLUS: lambda x,y:x+y,
    MINUS: lambda x,y:x-y,
    MUL: lambda x,y:x*y,
    DIV: lambda x,y:x//y,
}

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

        
        if text[self.pos] == '*':
            self.pos += 1
            return Token(MUL, '*')
            
        if text[self.pos] == '/':
            self.pos += 1
            return Token(DIV, '/s')

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
        while True:
            op = self.current_token
            if op.type == EOF: 
                break
            self.eat(op.type)
            # if op.type == PLUS:
            #     self.eat(PLUS)
            # elif op.type == MINUS:
            #     self.eat(MINUS)
            # elif op.type == MUL:
            #     self.eat(MUL)
            # elif op.type == DIV: 
            #     self.eat(DIV)
            
            right = self.current_token
            self.eat(INTEGER)

            left = Token(INTEGER, OPS[op.type](left.value,right.value))
        return left.value

def test_spaces():
    assert Interpeter('5 +   4').expr() == 9
    assert Interpeter('5 +4 ').expr() == 9
    assert Interpeter(' 5+ 4 ').expr() == 9


def test_long_numbers():
    assert Interpeter('55 + 4').expr() == 59


def test_arithmatics():
    assert Interpeter('55 + 4').expr() == 59
    assert Interpeter('55 - 4').expr() == 51
    assert Interpeter('55 * 4').expr() == 220
    assert Interpeter('40 / 4').expr() == 10


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
