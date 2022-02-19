from src.interpreter.interpreter import *

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
