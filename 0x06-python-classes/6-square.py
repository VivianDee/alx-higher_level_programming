#!/usr/bin/python3
"""The class Square"""


class Square:
    """Initialize the class with a size.

        Args:
            size (int): The size of the object. Defaults to 0.
            position (tuple): The position of the object. Defaults to 0.
        Raises:
            TypeError: If the size is not an integer.
            ValueError: If the size is less than 0.
        """
    def __init__(self, size=0, position=(0, 0)):
        if isinstance(size, int):
            self.__size = size
            self.__position = position
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
        """Sets the private instance size to value

            Args:
                value (int): The new size of the square

        """
        if isinstance(value, int):
            self.__size = value
        else:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    @property
    def position(self):
        """Returns the private instance position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the private instance position to value

            Args:
                value (tuple): The new position of the square

        """
        if isinstance(value, tuple) and len(value) == 2:
            if int(value[0]) > 0 and int(value[1]) > 0:
                self.__position = value
            else:
                raise TypeError("position must be a tuple of 2 positive integers")
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """Returns the area of the square"""
        return self.__size ** 2

    def my_print(self):
        """Prints in stdout the square with the character #"""
        if self.__size > 0:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
        else:
            print()
