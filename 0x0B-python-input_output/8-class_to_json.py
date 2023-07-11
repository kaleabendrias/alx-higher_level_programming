#!/usr/bin/python3
"""class yo json"""


def class_to_json(obj):
    """returns dic disc"""
    structure = {}
    if hasattr(obj, "__dict__"):
        structure = obj.__dict__.copy()
    return structure
