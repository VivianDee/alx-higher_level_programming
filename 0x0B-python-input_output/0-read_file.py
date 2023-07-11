#!/usr/bin/python3
"""This module contains the readfile function"""


def read_file(filename=""):
    """Reads a file and prints file content to stdout"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end='')
