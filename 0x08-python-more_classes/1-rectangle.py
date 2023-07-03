#!/usr/bin/python3
""" class rectangle that have some functionality"""


class Rectangle:
    """ class rect that has private attr height, width"""
    def __init__(self, width=0, height=0):
        """ initalizes private attr width, height"""
        self.__width = width
        self.__height =  height

    @property
    def width(self):
        """ getter for width """
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ getter for the height variable """
        return self.__height

    @height.setter
    def height(self, value):
        """ setter for priv var height """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
