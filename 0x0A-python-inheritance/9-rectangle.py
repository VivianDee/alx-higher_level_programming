#!/usr/bin/python3
"""
The class Rectangle
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry
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

    def area(self):
        """Calculates the area"""
        return self.__width * self.__height

    def __str__(self):
        """Return a string repreentstion of the rectangle"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
