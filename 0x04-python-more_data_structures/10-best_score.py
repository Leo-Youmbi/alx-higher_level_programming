#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    tup = tuple(a_dictionary.items())
    best = tup[0][1]
    for i in range(1, len(tup)):
        if tup[i][1] > best:
            best = tup[i][1]
            bestStudent = tup[i][0]
    return bestStudent
