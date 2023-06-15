#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    if a_dictionary is None:
        return None
    new_d = {k: x * 2 for k, x in a_dictionary.items()}
    return dic(new_d)
