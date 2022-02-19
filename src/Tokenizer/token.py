INTEGER, PLUS, MINUS, MUL, DIV, EOF, LBRACKET, RBRACKET = 'INTEGER', 'PLUS', 'MINUS', 'MUL', 'DIV', 'EOF', 'LBRACKET', 'RBRACKET'

class Token:
    def __init__(self, type, value) -> None:
        self.type = type
        self.value = value

    def __str__(self):
        return f"Token({self.type},{self.value})"

