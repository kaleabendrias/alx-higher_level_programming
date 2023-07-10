#!/usr/bin/python3
"""class module"""


class BaseGeometry:
    """ class Geometry"""

    def area(self):
        """raise exp area isnot implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """chrck if value is type int"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
