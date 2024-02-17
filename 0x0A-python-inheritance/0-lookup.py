#!/usr/bin/python3
def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.

    Args:
        obj: An object whose attributes and methods are to be looked up.

    Returns:
        list: A list of the names of attributes and methods of the object.
        """
    return dir(obj)
