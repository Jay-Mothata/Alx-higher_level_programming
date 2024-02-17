#!/usr/bin/python3
"""Student to JSON class"""


class Student:
    """ """
    def __init__(self, first_name, last_name, age):
        """
        Initializes a student object

        Args:
            first_name: student first name
            last_name: student last name
            age: student age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns the dictionary representation of student object"""
        return (self.__dict__)
