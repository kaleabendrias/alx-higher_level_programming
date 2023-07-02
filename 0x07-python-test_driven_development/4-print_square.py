#!/usr/bin/python3
""" prints # only accepts integer"""


def print_square(size):
    """prints square"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):
        print("#" * size)
