#!/usr/bin/python3

"""
The function inherits_from
"""

def inherits_from(obj, a_class):
    """
    Checks if an object is an instance of a subclass of a_class

    Args:
        obj: The object
        a_class: The class

    Returns:
        True if the object is an instance of a subclass of a_class
        False if the object is not an instance of a subclass of a_class
    """

    return issubclass(type(obj), a_class) and type(obj) is not a_class
