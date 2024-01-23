#!/usr/bin/python3
"""Defines a class Square with a private instance attribute size."""


class Square:
    """Class Square with a private instance attribute size."""

    def __init__(self, size):
        """Initializes a new Square instance.

        Args:
            size (int): The size of the square.
        """
        self.__size = size
