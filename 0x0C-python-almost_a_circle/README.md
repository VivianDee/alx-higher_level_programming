# Python - Almost a circle

This repository provides a collection of Python programs that cover various topics related to Python. Each program is designed to demonstrate and practice specific concepts and techniques. Here, you will find a brief overview of the topics covered in this repository, as well as a description of the tasks implemented in each program.

## Topics Covered

1. **Import**

2. **Exceptions**

3. **Class**

4. **Private attribute**

5. **Getter/Setter**

6. **Class method**

7. **Static method**

8. **Inheritance**

9. **Unittest**

10. **Read/Write file**

11. **args and kwargs**

12. **Serialization/Deserialization**

13. **JSON**


## Program Descriptions

Below is a brief description of each program included in this repository, along with the tasks implemented in each program.

1. **`models/__init__.py`**: This program is a Python package.



2. **`models/base.py`**: This program a class `Base` with a private class attribute `__nb_objects`, and initilises an intance variable `id`.

Static method `to_json_string` is introduced that returns the JSON string representation of list_dictionaries.

Class method `save_to_file` is introduced that writes the JSON string representation of list_objs to a file.

Static method `from_json_string` is introduced that returns the list of the JSON string representation json_string.

Class method `create` is introduced that returns an instance with all attributes already set.

Class method `load_from_file` is introduced that returns a list of instances.

Class methods `save_to_file_csv` and `load_from_file_csv` are introduce and they serializes and deserializes in CSV.

Static method `draw` is introduced that opens a window and draws all the Rectangles and Squares.



3. **`models/rectangle.py`**: This program defines a class `Rectangle` that inherits from `Base` initializing private instances `width`, `height`, `x` and `y`, each having a public getter and setter. It also adds validation of all setter methods and instantiation.

Public method `area` is introduced  that returns the area value of the Rectangle instance.

Public method `display` is introduced that prints in stdout the Rectangle instance with the character #.

`__str__` method is introduced which returns a string representation of the clsaa instance.

Public method `update` is introduced that assigns a key/value argument to each attribute.

Public method `to_dictionary` is introduced that returns the dictionary representation of the Rectangle class instance.



4. **`models/square.py`**: This program defines a class `Square` that inherits from `Rectangle` introducing a class constructor that initializes `size`, `id`, `x` and `y` and calls the super class with `height`, `width`, `x` and `y`.

A public getter and setter is created for the clasee instance `size`. It also adds validation to the method.

Public method `update` is introduced that assigns a key/value argument to each attribute.

Public method `to_dictionary` is introduced that returns the dictionary representation of the Square class instance.

