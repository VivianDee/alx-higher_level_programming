#!/usr/bin/python3

"""
    The class MyList
"""

class MyList(list):
    """
    MyList is inherits from list
    """

    def print_sorted(self):
        """Prints the sorted list"""
        print(sorted(self))
