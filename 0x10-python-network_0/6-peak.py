#!/usr/bin/python3
"""This module contains a function to find a peak (maximum) element 
in a list of unsorted integers."""

def find_peak(list_of_integers):
    """find peak element"""
    if len(list_of_integers) == 0:
        return None
    if len(list_of_integers) == 1:
        return (list_of_integers[0])
    low = 0
    high = len(list_of_integers) - 1
    while low < high:
        mid = (low + high) // 2
        mid_value = list_of_integers[mid]

        if mid_value > list_of_integers[mid+1]:
            high = mid
        else: 
            low = mid + 1

    return list_of_integers[low]