#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
"""
The class Square
"""


class Square(Rectangle):
    """
    Performs specified operations
    """

    def __init__(self, size):
        """
        Initializes the size

        Args:
            size: The size
        """
        super().__init__(size, size)
