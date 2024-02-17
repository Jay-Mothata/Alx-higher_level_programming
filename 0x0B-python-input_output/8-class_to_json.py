#!/usr/bin/python3
""" Class to JSON """


def class_to_json(obj):
    """
    Write a function that returns the dictionary description with
    simple data structure (list, dictionary, string, integer and boolean)
    for JSON serialization of an object

    Args:
        obj: an instance of a class

    Returns:
        reutns dict description of object with simple DS
    """
    return (obj.__dict__)
