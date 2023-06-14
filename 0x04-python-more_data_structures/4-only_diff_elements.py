#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    diff_elems = [x for x in set_1 if x not in set_2]
    diff2 = [y for y in set_2 if y not in set_1]
    return diff_elems + diff2
