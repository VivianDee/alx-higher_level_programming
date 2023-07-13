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

    def to_json(self, attrs=None):
        """Retreives a json string of the class instance"""

        result = self.__dict__

        if attrs is None:
            return result

        dictionary = {}
        for i in attrs:
            if i == 'first_name':
                dictionary[i] = result[i]
            if i == 'last_name':
                dictionary[i] = result[i]
            if i == 'age':
                dictionary[i] = result[i]
        return dictionary
