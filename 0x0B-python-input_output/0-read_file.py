#!/usr/bin/python3
"""
A function that reads a text file and prints to stdout
"""


def read_file(filename=""):
    """
    Read a text file and print its content to stdout.

    Args:
        filename: The path to the text file to be read. Default is empty string
    """
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="\n")
