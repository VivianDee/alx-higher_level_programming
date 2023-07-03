#!/usr/bin/python3
"""
A function that adds two numbers
"""


def add_integer(a, b=98):
    """Add two integers or floats.

    This function takes two parameters, `a` and `b`, and returns their sum after converting them to integers.
    If `b` is not provided, it defaults to 98.

    Parameters:
    - a (int or float): The first number to be added.
    - b (int or float, optional): The second number to be added. Defaults to 98.

    Raises:
    - TypeError: If either `a` or `b` is not an integer or float.

    Returns:
    - int: The sum of `a` and `b` after converting them to integers.
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
