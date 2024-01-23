#!/usr/bin/python3
"""Defines a class Square with a private instance attribute size."""


class Square:
    """Class Square with a private instance attribute size."""

    def __init__(self, size=0):
        """Initializes a new Square instance.

        Args:
            size (int): The size of the square (default is 0).
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Calculates and returns the area of the square."""
        return self.__size ** 2
