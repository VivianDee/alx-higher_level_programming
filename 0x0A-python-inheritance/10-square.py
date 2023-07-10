#!/usr/bin/python3
"""
The class Square
"""


Rectangle = __import__('9-rectangle').Rectangle


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
