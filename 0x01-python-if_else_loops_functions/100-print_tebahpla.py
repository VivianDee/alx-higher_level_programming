#!/usr/bin/python3
for i in range(0, 26):
    if (i % 2) > 0:
        num = 122 - i - 32
    else:
        num = 122 - i
    print("{}".format(chr(num)), end="")
