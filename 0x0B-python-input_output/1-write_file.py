#!/usr/bin/python3

"""This module contain the write function"""


def write_file(filename="", text=""):
    """Writes a string to a file"""
    with open(filename, mode="w", encoding="utf-8") as f:
        read_chars = f.write(text)
    return read_chars
