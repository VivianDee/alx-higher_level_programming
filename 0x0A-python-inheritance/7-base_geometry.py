#!/usr/bin/python3
"""
The class BaseGeometry
"""


class BaseGeometry:
    """
    Performs specified operations

    Raises:
        Exception: "area() is not implemented"
    """

    def area(self):
        """ Checks for the area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name=None, value=None):
        """Validates value"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
