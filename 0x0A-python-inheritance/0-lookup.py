#!/usr/bin/python3
""" lookup """


def lookup(obj):
    """returns list of available attr """
    return [i for i in dir(obj)]
