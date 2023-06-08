#!/usr/bin/python3

if __name__ == "__main__":
    """Print the addition of all arguments."""
    import sys

    sum = 0
    args = sys.argv[1:]
    numArgs = len(args)
    for i in range(numArgs):
        sum += int(args[i])
    print("{}".format(sum))
