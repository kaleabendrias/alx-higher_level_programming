#!/usr/bin/python3
"""sqaure class that has getter,setter and prints the sqaure with '#'"""


class Square:
    """define square"""
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """getter for size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """setter for varibale size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """returns area of square:"""
        return (self.__size ** 2)

    def my_print(self):
        """prints square with '#'"""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
