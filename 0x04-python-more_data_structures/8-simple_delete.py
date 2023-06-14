#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    newDict = a_dictionary
    if key in newDict.keys():
        del newDict[key]
    return newDict
