#!/usr/bin/python3

"""This module contains the from_json_string function"""


import json


def from_json_string(my_str):
    """Return the python representation of a json string"""
    return json.loads(my_str)
