#!/usr/bin/python3

"""The append_after function"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of text to a file at a position"""
    with open(filename, mode='r', encoding="utf-8") as f:
        text = f.readlines()
    with open(filename, mode='w', encoding="utf-8") as f:
        for line in text:
            f.write(line)
            if search_string in line:
                f.write(new_string)
