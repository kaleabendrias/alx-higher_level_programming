#!/usr/bin/python3
"""This module says hi to a name"""


def say_my_name(first_name, last_name=""):
    err_msg = "first_name must be a string or last_name must be a string"
    if not isinstance(first_name, str) or not isinstance(last_name, str):
        raise TypeError(err_msg)
    print("My name is", first_name, last_name)
