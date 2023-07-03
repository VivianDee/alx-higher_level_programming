#!/usr/bin/python3
"""The class Rectangle"""


class Rectangle:
    """Represents a Rectangle shape."""
    number_of_instances = 0
    print_symbol = "#"

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
        type(self).number_of_instances += 1

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
        if isinstance(self.print_symbol, str):
            string = ""
        else:
            string = []
        if self.__width > 0 and self.__height > 0:
            for i in range(self.__height):
                for j in range(self.__width):
                    if isinstance(self.print_symbol, str):
                        string += (self.print_symbol)
                    else:
                        string.append(self.print_symbol)
                string += "\n"
        else:
            string += "\n"
        return str(string[:-1])

    def __repr__(self):
        """Return a canonical string representation of the rectangle"""
        return str("Rectangle(" + str(self.__width) + ", "
                   + str(self.__height) + ")")

    def __del__(self):
        """Deletes an instance of the class"""
        print("Bye rectangle...")
        if self.number_of_instances > 0:
            type(self).number_of_instances -= 1

    def bigger_or_equal(rect_1, rect_2):
        """Returns the biggest rectangle based on the area"""
        if isinstance(rect_1, Rectangle):
            if isinstance(rect_2, Rectangle):
                area1 = rect_1.area()
                area2 = rect_2.area()
                if area1 >= area2:
                    return rect_1
                else:
                    return rect_2
            else:
                raise TypeError("rect_2 must be an instance of Rectangle")
        else:
            raise TypeError("rect_2 must be an instance of Rectangle")

    @classmethod
    def square(cls, size=0):
        """Returns a new Rectangle instance with width==height==size"""
        return cls(size, size)
