#!/usr/bin/python3
"""
A function that writes an Object to a text file,
using a JSON representation
"""
from json import dump


def save_to_json_file(my_obj, filename):
    """
    A function that writes an Object to a text file,
    using a JSON representation

    Args:
        my_obj: object to be saved
        filename: file to save into
    """
    with open(filename, mode='w', encoding="utf-8") as file:
        return dump(my_obj, file, sort_keys=True)
