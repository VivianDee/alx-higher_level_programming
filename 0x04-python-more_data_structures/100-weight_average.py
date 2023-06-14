#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None:
        return None
    weight1 = 0
    weight2 = 0
    for i, j in my_list:
        weight1 += i * j
        weight2 += j
    return weight1/weight2
