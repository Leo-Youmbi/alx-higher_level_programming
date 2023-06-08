#!/usr/bin/python3

if __name__ == "__main__":
    """Print the number of and list of arguments."""
    import sys

    args = sys.argv[1:]
    numArgs = len(args)

    if numArgs == 0:
        print("0 arguments.")
    elif numArgs == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(numArgs))
    for i in range(numArgs):
        print("{}: {}".format(i + 1, args[i]))
