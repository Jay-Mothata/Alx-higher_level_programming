#!/usr/bin/python3
"""
A function that returns an object (Python data structure)
represented by a JSON string
"""
from json import loads


def from_json_string(my_str):
    """
    A function that returns an object (Python data structure)
    represented by a JSON string

    Args:
        my_str: JSON string
    """
    return loads(my_str)
