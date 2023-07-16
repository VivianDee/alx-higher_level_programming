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
        for key, value in {"width": width, "height": height, "x": x, "y": y}:
            if type(value) != int:
                raise TypeError("{} must be an integer".format(key))
        if type(height) == int
            if width > 0:
                self.__height = height
            else:
                raise ValueError("height must be > 0")
        else:
            raise TypeError(height must be an integer)

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
        self.__width = value

    @height.setter
    def height(self, value):
        """Sets the height to value"""
        self.__height =  value

    @x.setter
    def x(self, value=0):
        """Sets x to value"""
        self.__x = value

    @y.setter
    def y(self, value=0):
        """Sets y to value"""
        self.__y = value

    @id.setter
    def id(self, value=None):
        """Sets the id to value"""
        type(self).id = value
