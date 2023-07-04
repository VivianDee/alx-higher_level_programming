#!/usr/bin/python3
"""
    Function say_my_name
"""


def say_my_name(first_name, last_name=""):
    """
    Prints the name by combining the first name and last name.

    Args:
        first_name (str): The first name.
        last_name (str, optional): The last name. Default is an empty string.

    Raises:
        TypeError: If first_name is not a string.
        TypeError: If last_name is not a string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    full_name = first_name + " " + last_name
    print("My name is", full_name)
