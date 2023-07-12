#!/usr/bin/python3

"""This module contains the load_from_json_file function"""


import json


def load_from_json_file(filename):
    """loads a jason object from a file"""
    with open(filename, mode='r', encoding="utf-8") as f:
        return json.load(f)
