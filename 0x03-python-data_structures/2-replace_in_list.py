#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """Replace an element at a particular index."""
    if idx in range(len(my_list)):
        my_list[idx] = element
    return my_list
