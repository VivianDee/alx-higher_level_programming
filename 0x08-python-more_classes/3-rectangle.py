#!/usr/bin/python3
"""The class Rectangle"""


class Rectangle:
    """Represents a Rectangle shape."""

    def __init__(self, width=0, height=0):
        """Initialize the class with a width and height.
           Args:
               height (int): The height.
               width (int): The width

           Raises:
               TypeError: If the height or width is not an integer.
               ValueError: If the height or width is less than 0.
        """
        if isinstance(height, int):
            self.__height = height
        else:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        if isinstance(width, int):
            self.__width = width
        else:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")

    @property
    def width(self):
        """Returns the width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the private instance width to value."""
        if isinstance(value, int):
            self.__width = value
        else:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        """Returns the height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the private instance height to value."""
        if isinstance(value, int):
            self.__height = value
        else:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

    def area(self):
        """Returns the rectangle area of the retangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the rectangle perimeter of the retangle."""
        if self.__width > 0 and self.__height > 0:
            return 2 * (self.__width + self.__height)
        else:
            return 0

    def __str__(self):
        """Return a string representation of the rectangle"""
        string = ""
        if self.__width > 0 and self.__height > 0:
            for i in range(self.__height):
                string += "#" * self.__width + "\n"
        else:
                string += "\n"
        return str(string[:-1])
