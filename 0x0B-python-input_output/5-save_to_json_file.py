#!/usr/bin/python3
"""writes an obj to a text file,on rep"""
import json


def save_to_json_file(my_obj, filename):
    """saves to json  file"""
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
