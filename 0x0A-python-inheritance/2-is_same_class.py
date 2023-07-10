#!/usr/bin/python3
""" checks class"""


def is_same_class(obj, a_class):
    """checks if same tyoe of obj"""
    if type(obj) is a_class:
        return True
    else:
        return False
