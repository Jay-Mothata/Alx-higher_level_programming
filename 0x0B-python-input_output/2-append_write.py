#!/usr/bin/python3
"""
A function that appends a string at the end of a text file (UTF8)
and returns the number of characters added.
"""


def append_write(filename="", text=""):
    """
    Append a str to the end of a text file and return the num of char added.

    Args:
        filename: The path to the text file to which the str will be appended.
        text: The string to be appended to the file.
    Returns:
        int: Number of characters added to the file.

    """
    with open(filename, mode="a", encoding="utf-8") as file:
        num_characters_added = file.write(text)
    return (num_characters_added)
