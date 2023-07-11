#!/usr/bin/python3
"""returns an obj rep by json string"""

import json


def from_json_string(my_str):
    """returns json"""
    x = json.loads(my_str)
    return x
