#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_d = {k: x * 2 for k, x in a_dictionary.items()}
    return new_d
