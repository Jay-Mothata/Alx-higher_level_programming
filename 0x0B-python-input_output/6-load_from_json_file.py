#!/usr/bin/python3
"""A function that creates an Object from a “JSON file”"""
from json import load


def load_from_json_file(filename):
    """
    A function that creates an Object from a “JSON file”

    Args:
        filename: file to load from
    """
    with open(filename) as file:
        return json.load(file)
