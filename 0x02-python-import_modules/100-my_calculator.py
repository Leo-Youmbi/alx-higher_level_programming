#!/usr/bin/python3

if __name__ == "__main__":
    """Handle basic arithmetic operations."""
    from calculator_1 import add, sub, mul, div
    import sys

    args = sys.argv[1:]
    numArgs = len(args)

    if numArgs != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(0)
    fnum = int(args[0])
    op = args[1]
    snum = int(args[2])
    match op:
        case '+':
            print("{} + {} = {}".format(fnum, snum, add(fnum, snum)))
            sys.exit(0)
        case '-':
            print("{} - {} = {}".format(fnum, snum, sub(fnum, snum)))
            sys.exit(0)
        case '*':
            print("{} * {} = {}".format(fnum, snum, mul(fnum, snum)))
            sys.exit(0)
        case '/':
            print("{} / {} = {}".format(fnum, snum, div(fnum, snum)))
            sys.exit(0)
        case _:
            print("Unknown operator:  Available operators: +, -, * and /")
            sys.exit(1)
