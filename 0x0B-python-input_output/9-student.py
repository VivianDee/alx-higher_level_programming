#!/usr/bin/python3
"""The class Student"""


class Student():
    """Defines a student by their first and ladt name, and age"""

    def __init__(self, first_name, last_name, age):
        """ 
        Initializes the firstname, lastname and age

        Args:
            firstname: The student's firstname 
            lastname: The student's last name
            age: The student's age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retreives a json string of the class instance"""
        return self.__dict__
