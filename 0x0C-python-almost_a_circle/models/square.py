#!/usr/bin/python3


"""The Square class"""

from models.rectangle import Rectangle



class Square(Rectangle):
    """Inherits from Class Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes the size, x, y, and id

        Args:
            size: size of Square
            x: A number
            y: A number
            id: id of the Square
        """
        super().__init__(size, size, x, y, id)
    def __str__(self):
        """Returns a string representation of the Square instance"""
        return "[{}] ({}) {}/{} - {}".format(
            self.__class__.__name__, self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """Returns the size"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute"""
        length = len(args)
        if length >= 1:
            type(self).id = args[0]
        if length >= 2:
            self.width = args[1]
        if length >= 3:
            self.height = args[2]
        if length >= 4:
            self.x = args[3]
        if length >= 5:
            self.y = args[4]
        if length == 0 and kwargs is not None:
            for key, val in kwargs.items():
                if key == "width":
                    self.width = val
                if key == "height":
                    self.height = val
                if key == "x":
                    self.x = val
                if key == "y":
                    self.y = val
                if key == "id":
                    self.id = val

    def to_dictionary(self):
         """Returns the dictionary representation of a Square"""
         return {"width": self.width, "height": self.height, "x": self.x, "y": self.y, "id": self.id}
