#!/usr/bin/python3
def remove_char_at(str, n):
    string = list(str)
    if n >= 0 and n <= len(str):
        string.pop(n)
    return "" .join(string)
