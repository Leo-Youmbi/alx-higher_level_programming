#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    sortedDictList = sorted(a_dictionary.keys())
    for key in sortedDictList:
        print("{}: {}".format(key, a_dictionary[key]))
