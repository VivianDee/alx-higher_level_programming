#!/usr/bin/python3

"""The add_attr function"""


def add_attribute(obj, name, value):
    """Adds a new attribute to an object if its possible"""
    try:
        setattr(obj, name, value)
    except Exception:
        raise TypeError("can't add new attribute")
