#!/usr/bin/python3


"""The Base class"""


import json
import csv


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

    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of list_dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file
        """
        filename = cls.__name__ + ".json"
        with open(filename, 'w') as f:
            if list_objs is None:
                f.write("[]")
            else:
                json_string = json.dumps([obj.to_dictionary()
                                          for obj in list_objs])
                f.write(json_string)

    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = cls()

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r') as f:
                json_string = f.read()
                dictionary_list = cls.from_json_string(json_string)
                instances = [cls.create(**obj) for obj in dictionary_list]
                return instances
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes in CSV"""
        filename = cls.__name__ + ".csv"
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            if cls.__name__ == "Rectangle":
                writer.writerow(["id", "width", "height", "x", "y"])
            elif cls.__name__ == "Square":
                writer.writerow(["id", "size", "x", "y"])
            else:
                raise ValueError(f"Unsupported class: {cls.__name__}")

            for obj in list_objs:
                writer.writerow(obj.to_dictionary().values())

    @classmethod
    def load_from_file_csv(cls):
        """Deserializes in CSV"""
        filename = cls.__name__ + ".csv"
        instances = []
        with open(filename, 'r') as csvfile:
            reader = csv.reader(csvfile)
            header = next(reader)  # Skip the header
            for row in reader:
                dictionary = {}
                if cls.__name__ == "Rectangle":
                    dictionary = {
                        "id": int(row[0]),
                        "width": int(row[1]),
                        "height": int(row[2]),
                        "x": int(row[3]),
                        "y": int(row[4])
                    }
                elif cls.__name__ == "Square":
                    dictionary = {
                        "id": int(row[0]),
                        "size": int(row[1]),
                        "x": int(row[2]),
                        "y": int(row[3])
                    }
                instance = cls.create(**dictionary)
                instances.append(instance)
        return instances
