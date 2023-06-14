#!/usr/bin/python3
def complex_delete(a_dictionary: dict, value):
    newDict = a_dictionary
    keys = a_dictionary.copy().keys()
    for key in keys:
        if newDict[key] == value:
            del newDict[key]
    return newDict
