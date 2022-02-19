from src.tokenizer.tokenizer import *
OPS = {
    PLUS: lambda x, y: x+y,
    MINUS: lambda x, y: x-y,
    MUL: lambda x, y: x*y,
    DIV: lambda x, y: x//y,
}
class Interpreter:
    def __init__(self, text: str) -> None:
        self.tokenizer = Tokenizer(text)
        self.current_token: Token = self.tokenizer.get_next_token()


    def skip_white_space(self):
        while self.pos < len(self.text) and self.text[self.pos].isspace():
            self.pos += 1



    def eat(self, token_type):
        if self.current_token.type == token_type:
            self.current_token = self.tokenizer.get_next_token()
        else:
            raise Exception("Invalid Syntax")
    
    def factor(self):
        """factor : INTEGER"""
        token = self.current_token
        if token.type == INTEGER:
            self.eat(INTEGER)
            return token
        elif token.type == LBRACKET:
            self.eat(LBRACKET)
            result = self.expr()
            self.eat(RBRACKET)
            return Token(INTEGER,result)

    def term(self):
        """term : factor((DIV|MUL)factor)*"""
        result = self.factor()

        while self.current_token.type in (MUL, DIV):
            op = self.current_token
            self.eat(op.type)
            right = self.factor()

            result = Token(INTEGER, OPS[op.type](result.value, right.value))
        return result

    def expr(self):
        """expr : term((PLUS|MINUS)term)*"""

        # self.current_token = self.get_next_token()
        result = self.term()

        while self.current_token.type in (PLUS, MINUS):
            op = self.current_token
            self.eat(op.type)
            right = self.term()

            result = Token(INTEGER, OPS[op.type](result.value, right.value))

        return result.value

