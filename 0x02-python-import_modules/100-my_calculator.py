#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    lsn = len(sys.argv)
    if lsn != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    if sys.argv[2] != '+' and sys.argv[2] != '/' and sys.argv[2] != '*' and sys.argv[2] != '-':
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    elif sys.argv[2] == '+':
        res = add(int(sys.argv[1]), int(sys.argv[3]))
    elif sys.argv[2] == '-':
        res = sub(int(sys.argv[1]), int(sys.argv[3]))
    elif sys.argv[2] == '*':
        res = mul(int(sys.argv[1]), int(sys.argv[3]))
    elif sys.argv[2] == '/':
        res = div(int(sys.argv[1]), int(sys.argv[3]))
    print(f"{sys.argv[1]} {sys.argv[2]} {sys.argv[3]} = {res}")
