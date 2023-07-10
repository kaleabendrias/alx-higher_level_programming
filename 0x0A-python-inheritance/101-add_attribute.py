#!/usr/bin/python3
"""method module"""


def add_attribute(obj, objname, value):
    """adds atrr to obj else raises ex"""
    if hasattr(obj, "__dict__") == False:
        raise TypeError("can't add new attribute")
    setattr(obj, objname, value)
