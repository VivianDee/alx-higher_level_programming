#!/usr/bin/python3

"""This module contains the save_to_json_file function"""


import json


def save_to_json_file(my_obj, filename):
    """Saves a jason object to a file"""
    with open(filename, mode='w', encoding="utf-8") as f:
        json.dump(my_obj, f)
