#!/usr/bin/python3
"""The MyInt Function"""


class MyInt(int):
    """
    A class that inherits from int
    """

    def __eq__(self, x):
        """Replace __ne__ magic class"""
        return super().__ne__(x)

    def __ne__(self, x):
        """Replace the __eq__ magic class"""
        return super().__eq__(x)
