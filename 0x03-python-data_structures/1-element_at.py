#!/usr/bin/python3
def element_at(my_list, idx):
    """Get an element at a particular index."""
    if idx not in range(len(my_list)):
        return None
    return my_list[idx]
