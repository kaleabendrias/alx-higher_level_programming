#!/usr/bin/python3
"""method """


def inherits_from(obj, a_class):
    """ cheaks if obj is instance of class"""
    if type(obj) == a_class:
        return False
    return issubclass(type(obj), a_class)
