#!/usr/bin/python3
"""returns json rep of obj"""
import json


def to_json_string(my_obj):
    """returns json rep"""
    x = json.dumps(my_obj)
    return x
