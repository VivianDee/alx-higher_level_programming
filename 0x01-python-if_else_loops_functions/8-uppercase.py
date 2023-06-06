#!/usr/bin/python3
def uppercase(str):
    for letter in str:
        num = ord(letter)
        if num > 96 and num < 123:
            print("{}".format(chr(num - 32)), end="")
        else:
            print("{}".format(letter), end="")
    print()
