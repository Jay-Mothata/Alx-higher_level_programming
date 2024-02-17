#!/usr/bin/python3
"""Student to JSON class"""


class Student:
    """ """
    def __init__(self, first_name, last_name, age):
        """
        Initialize a student object

        Args:
            first_name: student first name
            last_name: student last name
            age: student age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns a dictionary represnetation of student object

        Args:
            attrs: list of attributes
        """
        if (attrs is not None):
            dict_rep = {}
            for attr in attrs:
                if hasattr(self, attr):
                    dict_rep[attr] = getattr(self, attr)
            return dict_rep
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """
        Replaces all attrs of student object

        Args:
            json: dictionary contains name and value attrs
        """
        for (key, value) in json.items():
            setattr(self, key, value)
