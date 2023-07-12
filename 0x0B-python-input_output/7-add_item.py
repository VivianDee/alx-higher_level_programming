#!/usr/bin/python3

"""The add_item function"""


import sys
import json


def add_item():
    """adds a comand line argument to a json file"""

    load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

    arg_list = []
 
    for i in range(1, len(sys.argv)):
        arg_list.append(sys.argv[i])

    try:
        file_list = load_from_json_file("add_item.json")
        arg_list = file_list + arg_list
    except:
        pass
    save_to_json_file(arg_list, "add_item.json")


add_item()
