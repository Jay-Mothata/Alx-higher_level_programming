#!/usr/bin/python3
"""
A function that writes a string to a text file (UTF8)
and returns the number of characters written.
"""


def write_file(filename="", text=""):
    """
    Write string to a text file and return the number of characters written.

    Args:
        filename: The path to the text file to be written.
        text: The string to be written to the file.

    Returns:
        int: Number of characters written to the file.

    """
    with open(filename, mode="w", encoding="utf-8") as file:
        num_characters = file.write(text)
    return (num_characters)
