#!/usr/bin/python3

"""The class_to_json function"""


def class_to_json(obj):
    """Returns the dictionary description of a class instance"""
    return obj.__dict__
