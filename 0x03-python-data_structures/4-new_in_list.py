#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """Replace an element at a particular index in a copied list."""
    if idx not in range(len(my_list)):
        return my_list
    newList = [i for i in my_list]
    newList[idx] = element
    return newList
