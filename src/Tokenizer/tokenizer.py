from .token import *
TOKENS = {
    '+': Token(PLUS, '+'),
    '-': Token(MINUS, '-'),
    '*': Token(MUL, '*'),
    '/': Token(DIV, '/'),
    '(': Token(LBRACKET, '('),
    ')': Token(RBRACKET, ')')
}
class Tokenizer:
    def __init__(self, text: str) -> None:
        self.text: str = text
        self.pos = 0
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

        if text[self.pos] in TOKENS.keys():
            token = TOKENS[text[self.pos]] 
            self.pos += 1
            return token

        self.error()

    def error(self):
        raise Exception("Invalid Syntax")
    
    def skip_white_space(self):
        while self.pos < len(self.text) and self.text[self.pos].isspace():
            self.pos += 1

    def parse_integer(self):
        """
        parse integer number that appers in text
        """
        number = ""
        while self.pos < len(self.text) and self.text[self.pos].isdigit():
            number += self.text[self.pos]
            self.pos += 1
        return number
