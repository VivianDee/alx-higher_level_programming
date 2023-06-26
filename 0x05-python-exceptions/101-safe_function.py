#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        result = fct(*args) 
    except Exception as ne:
        print("Exception: {}".format(ne), file=sys.stderr)
        return None
    else:
        return result
