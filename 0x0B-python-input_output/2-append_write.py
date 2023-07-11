#!/usr/bin/python3

"""This module contains the append function"""


def append_write(filename="", text=""):
    """Writes a string to a file"""
    with open(filename, mode="a", encoding="utf-8") as f:
        read_chars = f.write(text)
    return read_chars
