#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value), end="")
    except Exception as ne:
        print("Exception: {}".format(ne), file=sys.stderr)
        return False
    else:
        print()
        return True
