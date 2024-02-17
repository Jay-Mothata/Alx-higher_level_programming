#!/usr/bin/python3
"""
A function that returns the JSON representation
of an object (string)
"""


def to_json_string(my_obj):
    """
    A function that returns the JSON representation
    of an object (string)

    Args:
        my_obj: object to be converted to JSON
    """
    import json
    if isinstance(my_obj, dict):
        return (json.dumps(
               {key: my_obj[key] for key in sorted(my_obj)},
               sort_keys=True)
        )
    else:
        return (json.dumps(my_obj))
