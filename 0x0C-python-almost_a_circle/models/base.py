#!/usr/bin/python3


"""The Base class"""


class Base:
    """Acts as a “base” of all other classes in this project"""
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes the instance attribute id
        
        Args:
            id: The id of the class instance
        """ 
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
