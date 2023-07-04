#!/usr/bin/python3
"""
    Function print_square
"""


def print_square(size):
    """
    Prints in stdout the square with the character #

    Args:
        size (int, optional): The size of the square.

    Raises:
        TypeError: if size is not an integer.
        ValueError: if size is less than zero.
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size == 0:
        return ""
    if size > 0:
        if type(size) is float and size < 0:
            raise TypeError("size must be an integer")
        for i in range(size):
            print("#" * size)
    else:
        raise ValueError("size must be >= 0")
