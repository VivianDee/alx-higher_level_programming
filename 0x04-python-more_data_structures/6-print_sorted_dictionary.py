#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    for key in sorted(list(a_dictionary.keys())):
        value = a_dictionary.get(key)
        print("{:s} : {}".format(key, value))
