#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """Find all multiples of 2 in a list."""
    resultList = []
    for i in my_list:
        resultList.append(i % 2 == 0)
    return resultList
