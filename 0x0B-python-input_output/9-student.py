#!/usr/bin/python3
"""class Student"""


class Student:
    """class student"""

    def __init__(self, first_name, last_name, age):
        """init method"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """returns disc discription"""
        return self.__dict__.copy()
