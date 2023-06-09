#!/usr/bin/python3
def no_c(my_string):
    """Removes all 'C's and c's in the string."""
    newStr = ""
    for char in my_string:
        if char == 'C' or char == 'c':
            continue
        newStr += char
    return newStr
