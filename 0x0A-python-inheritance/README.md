# Python - Inheritance

This repository provides a collection of Python programs that cover various topics related to Python classes and objects. Each program is designed to demonstrate and practice specific concepts and techniques. Here, you will find a brief overview of the topics covered in this repository, as well as a description of the tasks implemented in each program.

## Topics Covered

1. **Object Oriented Programming (OOP):** 

2. **Inheritance**

3. **Multiple inheritance**

4. **Inheritance in Python**

5. **Learn to Program 10 : Inheritance Magic Methods**

## Program Descriptions

Below is a brief description of each program included in this repository, along with the tasks implemented in each program.

1. **`0-lookup.py`**: This program returns the list of available attributes and methods of an object: `lookup`.

2. **`1-my_list.py`**: This program defines a class `MyList` that inherits from list. Public instance method: `print_sorted(self)` prints the list, but sorted (ascending sort)

3. **`2-is_same_class.py`**: This program defines a function `is_same_class(obj, a_class)` that returns True if the object is exactly an instance of the specified class ; otherwise False.

4. **`3-is_kind_of_class.py`**: This program defines a function `is_kind_of_class(obj, a_class)` that returns True if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class ; otherwise False.

5. **`4-inherits_from.py`**: This program defines a function `inherits_from(obj, a_class)` that returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise False.

6. **`5-base_geometry.py`**: This program defines an empty class `BaseGeometry`.

7. **`6-base_geometry.py`**: This program defines a class `BaseGeometry` (based on 5-base_geometry.py), introducing a public instance method `area` that raises an Exception with the message "area() is not implemented".

8. **`7-base_geometry.py`**: This program defines a class `BaseGeometry` (based on 6-base_geometry.py), introducing a new public instance method `integer_validator` that validates a value.

9. **`8-rectangle.py`**: This program defines a class `Rectangle` that inherits from calss `BaseGeometry` (7-base_geometry.py), initializing the `width` and `height`.

10. **`9-rectangle.py`**: This program defines a class `Rectangle` (based on 8-rectangle.py), introducing a public instance method `area`. The class should return the rectangle description.

11. **`10-square.py`**: This program defines a class `Square` that inherits from calss `Rectangle` (9-rectangle.py), initializing the `size` and introducing a public instance method `area`.

12. **`11-square.py`**: This program defines a class `Square` (based on 10-square.py). The class should return the square description.
