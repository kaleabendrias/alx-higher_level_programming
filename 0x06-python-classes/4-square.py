#!/usr/bin/python3
"""square class that has getter and setter for its size and returns area"""


class Square:
    """define square"""
    def __init__(self, size=0):
        """intialize """
        self.__size = size

    @property
    def size(self):
        """getter for size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """setter for size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """return area"""
        return (self.__size ** 2)
