#!/usr/bin/python3
def no_c(my_string):
    str1 = ""
    new_string = []
    for i in my_string:
        if i == "c" or i == "C":
            continue
        new_string.append(i)
    return str1.join(new_string)
