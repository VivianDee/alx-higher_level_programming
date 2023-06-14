#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    x = 0
    val = max(a_dictionary.values())
    n = {key: value for key, value in a_dictionary.items() if value == val}
    result = list(n)
    return result[0]
