#!/usr/bin/python3
""" class Rectangle that has area and perimeter"""


class Rectangle:
    """ Rectangle class that returns area and perimeter"""
    def __init__(self, width=0, height=0):
        """ initalize height and width"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ returns width"""
        return self.__width

    @width.setter
    def width(self, value):
        """" sets the width to new val"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ getter fot heigth"""
        return self.__height

    @height.setter
    def height(self, value):
        """ sets height """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ obj method
        Returns:
            area of tringle
        """
        return self.__width * self.__height

    def perimeter(self):
        """ obj methos
        Returns:
            rectangle's perimter
        """
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """prints rectangles"""
        if self.__height == 0 or self.__width == 0:
            return ""
        new_str = ""
        for i in range(self.__height):
            for j in range(self.__width):
                new_str += "#"
            new_str += "\n"
        return new_str[:-1]

    def __repr__(self):
        """ returns a rep of rectangle """
        return "{}({}, {})".format((type(self).__name__), self.__width, self.__height)
