#!/usr/bin/python3
"""class square that returns the area"""


class Square:
    """define Square"""
    def __init__(self, size=0):
        """initalize it"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """returns the area of square"""
        return (self.__size * self.__size)
