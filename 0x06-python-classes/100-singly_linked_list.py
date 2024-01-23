#!/usr/bin/python3
"""Defines a Node and a SinglyLinkedList."""


class Node:
    """Class Node that defines a node of a singly linked list."""

    def __init__(self, data, next_node=None):
        """Initializes a new Node instance.

        Args:
            data (int): The data of the node (must be an integer).
            next_node (Node): The next node in the linked list.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Getter method to retrieve the data of the node."""
        return self.__data

    @data.setter
    def data(self, value):
        """Setter method to set the data of the node.

        Args:
            value (int): The data value to be set.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """Getter method to retrieve the next node in the linked list."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Setter method to set the next node in the linked list.

        Args:
            value (Node): The next node to be set.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """Class SinglyLinkedList that defines a singly linked list."""

    def __init__(self):
        """Initializes a new SinglyLinkedList instance."""
        self.head = None

    def sorted_insert(self, value):
        """Inserts a new Node into the correct sorted position in the list.

        Args:
            value (int): The value of the node to be inserted.
        """
        new_node = Node(value)
        if self.head is None or value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node is not None and \
                    current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """String representation of the linked list."""
        result = ""
        current = self.head
        while current is not None:
            result += str(current.data) + "\n"
            current = current.next_node
        return result
