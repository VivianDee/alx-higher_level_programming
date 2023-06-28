#!/usr/bin/python3
"""The class Square"""


class Square:
    """Initialize the class with a size.

        Args:
            size (int, optional): The size of the object. Defaults to 0.

        Raises:
            TypeError: If the size is not an integer.
            ValueError: If the size is less than 0.
        """
    def __init__(self, size=0):
        if isinstance(size, int):
            self.__size = size
        else:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    @property
    def size(self):
        """Returns the private instance size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the private instance size to value"""
        if isinstance(value, int):
            self.__size = value
        else:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Returns the area of the square"""
        return self.__size ** 2

    def __eq__(self, other):
        """Checks if two squares have the same area"""
        if isinstance(other, Square):
            return self.area() == other.area()
        return False

    def __ne__(self, other):
        """Checks if two squares do not have the same area"""
        return not self.__eq__(other)

    def __gt__(self, other):
        """Checks if one area is greater"""
        if isinstance(other, Square):
            return self.area() > other.area()
        return False

    def __ge__(self, other):
        """Checks if one area is greater or equal to"""
        if isinstance(other, Square):
            return self.area() >= other.area()
        return False

    def __lt__(self, other):
        """Checks if one area is less"""
        if isinstance(other, Square):
            return self.area() < other.area()
        return False

    def __le__(self, other):
        """Checks if one area is less or equal to"""
        if isinstance(other, Square):
            return self.area() <= other.area()
        return False
