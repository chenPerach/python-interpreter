
from sys import exec_prefix


INTEGER, PLUS, EOF = 'INTEGER', 'PLUS', 'EOF'

class Token:
    def __init__(self,type,value) -> None:
        self.type = type
        self.value = value
    
    def __str__(self):
        return f"Token({self.type},{self.value})"


class Interpeter:
    def __init__(self,text : str) -> None:
        self.text : str= text
        self.pos = 0
        self.current_token : Token= None
    def error(self):
        raise Exception("Error parsing input")
    def get_next_token(self):
        """
        returns the next token in the text
        """
        text = self.text

        if self.pos > len(text)-1:
            self.pos += 1
            return Token(EOF,None)

        if text[self.pos].isdigit():
            t = Token(INTEGER,int(text[self.pos]))
            self.pos += 1
            return t
        
        if text[self.pos] == '+':
            self.pos += 1
            return Token(PLUS,'+')
        self.error()
        
    def eat(self,token_type):
        if self.current_token.type == token_type:
            self.current_token = self.get_next_token()
        else:
            self.error()

    
    def expr(self):

        self.current_token = self.get_next_token()

        left = self.current_token
        self.eat(INTEGER)

        op = self.current_token
        self.eat(PLUS)

        right = self.current_token
        self.eat(INTEGER)

        return left.value + right.value




def main():
    while True:
        try:
            text = input(">>>")
        except EOFError:
            break

        if not text:
            continue
        interpeter = Interpeter(text)
        res = interpeter.expr()
        print(res)
if __name__ == "__main__":
    main()