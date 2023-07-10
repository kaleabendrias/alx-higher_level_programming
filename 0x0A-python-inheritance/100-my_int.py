#!/usr/bin/python3
"""class module"""


class MyInt(int):
    """class inherted the int"""

    def __eq__(self, other):
        """equal overidden with ne"""
        return super().__ne__(other)

    def __ne__(self, other):
        """ne overridden with ee"""
        return super().__eq__(other)
