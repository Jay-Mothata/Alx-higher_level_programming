#!/usr/bin/python3
"""Defines a class Square."""


class Square:
    """Class Square that defines a square."""

    def __init__(self, size=0):
        """Initializes a new Square instance.

        Args:
            size (number): The size of the square (default is 0).
        """
        self.size = size

    @property
    def size(self):
        """Getter method to retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method to set the size of the square.

        Args:
            value (number): The size value to be set.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Calculates and returns the area of the square."""
        return self.__size ** 2

    def __eq__(self, other):
        """Equality comparator based on square area."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Inequality comparator based on square area."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Less than comparator based on square area."""
        return self.area() < other.area()

    def __le__(self, other):
        """Less than or equal to comparator based on square area."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Greater than comparator based on square area."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Greater than or equal to comparator based on square area."""
        return self.area() >= other.area()
