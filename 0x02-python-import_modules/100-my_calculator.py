#!/usr/bin/python3

if __name__ == "__main__":
    """Handle basic arithmetic operations."""
    from calculator_1 import add, sub, mul, div
    import sys

    args = sys.argv[1:]
    numArgs = len(args)

    if numArgs != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    fnum = int(args[0])
    op = args[1]
    snum = int(args[2])
    ops = {"+": add, "-": sub, "*": mul, "/": div}
    if op not in ops.keys():
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    print("{} {} {} = {}".format(fnum, op, snum, ops[op](fnum, snum)))
    sys.exit(0)
