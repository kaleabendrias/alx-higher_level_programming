#!/usr/bin/python3
""" locked class"""


class LockedClass():
    """ locked class that wont let u create instance """
    __slots__ = ["first_name"]

    def __init__(self, first_name=""):
        self.first_name = first_name
