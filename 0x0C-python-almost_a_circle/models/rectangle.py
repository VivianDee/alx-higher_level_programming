#!/usr/bin/python3


"""The Rectangle class"""

from models.base import Base



class Rectangle(Base):
    """Inherits from Class Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes the width, heigth, x, y, and id

        Args:
            width: width of Rectangle
            height: height of Rectangle
            x: A number
            y: A number

        Raises:
            Typeerror: If the input is not an integer
            ValueError: If the input is less than or equal to 0
        """
        for key, value in ({"width": width, "height": height, "x": x, "y": y}).items():
            if type(value) != int:
                raise TypeError("{} must be an integer".format(key))
        for key, value in ({"width": width, "height": height}).items():
            if value <= 0:
                raise ValueError("{} must be > 0".format(key))
        for key, value in ({"x": x, "y": y}).items():
            if value < 0:
                raise ValueError("{} must be >= 0".format(key))
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """Returns the width"""
        return self.__width

    @property
    def height(self):
        """Returns the height"""
        return self.__height

    @property
    def x(self):
        """Returns x"""
        return self.__x

    @property
    def y(self):
        """Returns y"""
        return self.__y

    @property
    def id(self):
        """Returns the id"""
        return type(self).id

    @width.setter
    def width(self, value):
        """Sets the width to value"""
        if type(value) != int:
            raise TypeError("width must be an integer")

        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Sets the height to value"""
        if type(value) != int:
            raise TypeError("height must be an integer")

        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height =  value

    @x.setter
    def x(self, value=0):
        """Sets x to value"""
        if type(value) != int:
            raise TypeError("x must be an integer")

        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value=0):
        """Sets y to value"""
        if type(value) != int:
            raise TypeError("y must be an integer")

        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    @id.setter
    def id(self, value=None):
        """Sets the id to value"""
        type(self).id = value

    def area(self):
        """Returns the area of the Rectangle instance"""
        return self.__width * self.__height

    def display(self):
        """
        Prints a representation of the Rectangle instance
        with the character #
        """
        for i in range(0, self.__height):
            print("#" * self.__width)

    def __str__(self):
        """Returns a string representation of the Rectangle instance"""
        return "[{}] ({}) {}/{} - {}/{}".format(self.__class__.__name__, type(self).id, self.__x, self.__y, self.__width, self.__height)

    def display(self):
        """
        Prints a representation of the Rectangle instance
        with the character # by taking care of x and y
        """
        for i in range(0, self.__y):
            print( )
        for i in range(0, self.__height):
            print(' ' * self.__x + "#" * self.__width)

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute"""
        length = len(args)
        if length >= 1:
            type(self).id = args[0]
        if length >= 2:
            self.__width = args[1]
        if length >= 3:
            self.__height = args[2]
        if length >= 4:
            self.__x = args[3]
        if length >= 5:
            self.__y = args[4]
        if length == 0 and kwargs is not None:
            for key, val in kwargs.items():
                if key == "width":
                    self.__width = val
                if key == "height":
                    self.__height = val
                if key == "x":
                    self.__x = val
                if key == "y":
                    self.__y = val
                if key == "id":
                    type(self).id = val

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle"""
        return {"width": self.__width, "height": self.__height, "x": self.__x, "y": self.__y, "id": type(self).id}
