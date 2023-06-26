#!/usr/bin/python3

def safe_print_integer(value):
    state = True
    try:
        print("{:d}".format(value))
    except (ValueError, TypeError):
        state = False
    return state
