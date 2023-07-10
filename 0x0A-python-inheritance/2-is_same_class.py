#!/usr/bin/python3

"""
    The is_same_class function
"""


def is_same_class(obj, a_class):
    """
        Checks if obj is an instance of a_class

        Args:
             obj: The object
             a_class: The class

        Returns:
            True if the object is an instance of the class
            False if the object is not an instance of the class
    """
    if type(obj) == a_class:
        return True

    return False
