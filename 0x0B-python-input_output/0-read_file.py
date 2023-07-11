#!/usr/bin/python3
"""method that reads"""


def read_file(filename=""):
    """reads a file"""
    with open(filename) as f:
        for line in f:
            print(line, end="")
