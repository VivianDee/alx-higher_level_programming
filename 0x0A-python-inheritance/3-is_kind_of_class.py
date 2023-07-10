#!/usr/bin/python3

"""
The function is_kind_of_class
"""

def is_kind_of_class(obj, a_class):
    """
    Checks if an object is a kind of instance of the specified class

    Args:
        obj: The object
        a_class: The class

    Returns:
        True if the object is a kind of instance of the class
        False if the object is not a kind of instance of the class
    """

    if isinstance(obj, a_class):
        return True

    return False
