#!/usr/bin/python3
"""start module"""
import json


def load_from_json_file(filename):
    """loads from json"""
    with open(filename) as f:
        json.load(f)
