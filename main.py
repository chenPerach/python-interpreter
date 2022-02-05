
INTEGER, PLUS, EOF = 'INTEGER', 'PLUS', 'EOF'

class Token:
    def __init__(self,type,value) -> None:
        self.type = type
        self.value = value
    
    def __str__(self):
        return f"Token({self.type},{self.value})"


class Interpeter:
    def __init__(self,text) -> None:
        pass





def main():
    pass
if __name__ == "__main__":
    main()