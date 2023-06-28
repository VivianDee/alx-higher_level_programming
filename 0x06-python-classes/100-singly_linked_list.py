#!/usr/bin/python3
"""The class Node defines a node of a singly linked list"""


class Node:
    """Initialize the class with data and next_node.

        Args:
            data (int): The data of the object. Defaults to 0.
            next_node (int): The next node of the object. Defaults to 0.
        """
    def __init__(self, data=0, next_node=None):
        if isinstance(data, int):
            self.__data = data
        else:
            raise TypeError("data must be an integer")
        if isinstance(next_node, Node) or next_node is None:
            self.__next_node = next_node
        else:
            raise TypeError("next_node must be a Node object")

    @property
    def data(self):
        """Returns the private instance data"""
        return self.__data

    @data.setter
    def data(self, value):
        """Sets the private instance data to value

            Args:
                value (int): The new data of the square

        """
        if isinstance(value, int):
            self.__data = value
        else:
            raise TypeError("data must be an integer")

    @property
    def next_node(self):
        """Returns the private instance next_node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Sets the private instance next_node to value

            Args:
                value (int): The new next_node of the square

        """
        if isinstance(value, Node) or value is None:
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


"""The class SinglyLinkedList defines a singly linked list"""


class SinglyLinkedList:
    """Class SinglyLinkedList creates the linked list."""

    def __init__(self):
        """Initialize the class with head."""
        self.__head = None

    def sorted_insert(self, value):
        """sorted_insert inserts nodes in the linked list"""
        node = Node(value)

        if self.__head is None or value < self.__head.data:
            node.next_node = self.__head
            self.__head = node
        else:
            current = self.__head
            while current.next_node is not None and value >= current.next_node.data:
                current = current.next_node

            node.next_node = current.next_node
            current.next_node = node

    def __str__(self):
        """__str__ prints out the linked list"""
        listt = ""
        head = self.__head
        while head is not None:
            listt += str(head.data)
            head = head.next_node
            listt += "\n"
        return listt[:-1]
