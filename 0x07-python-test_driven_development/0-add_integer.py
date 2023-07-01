#!/usr/bin/python3

def add_integer(a, b=98):
    """A function that adds two integers

    Args:
        a (int): An number to add
        b (int, optional): A number to add. Defaults to 98.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
