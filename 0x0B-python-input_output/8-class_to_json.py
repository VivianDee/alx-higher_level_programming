#!/usr/bin/python3

"""The class_to_json function"""


import json


def class_to_json(obj):
    """Returns the dictionary description of a class instance"""
    return json.dumps(obj.__dict__)
