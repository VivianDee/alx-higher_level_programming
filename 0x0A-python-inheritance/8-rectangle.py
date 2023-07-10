#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""
The class Rectangle
"""


class Rectangle(BaseGeometry):
    """
    Performs specified operations
    """

    def __init__(self, width, height):
        """
        Initializes the width and height

        Args:
            width: The width
            height: The height
        """
        super().integer_validator("height", height)
        super().integer_validator("width", width)

        self.__width = width
        self.__height = height
