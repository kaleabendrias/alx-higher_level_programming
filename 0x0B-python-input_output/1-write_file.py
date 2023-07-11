#!/usr/bin/python3
"""writes a string totext file"""


def write_file(filename="", text=""):
    """writes to file and returns len"""
    with open(filename, 'w') as f:
        num = f.write(text)
    return (num)