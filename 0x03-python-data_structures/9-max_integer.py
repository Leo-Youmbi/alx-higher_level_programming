#!/usr/bin/python3
def max_integer(my_list=[]):
    """Returns the maximum integer value."""
    if my_list == []:
        return None
    maxInt = my_list[0]
    for i in range(1, len(my_list)):
        if maxInt < my_list[i]:
            maxInt = my_list[i]
    return maxInt
