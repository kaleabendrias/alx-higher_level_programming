#!/usr/bin/python3
"""class rectangle"""

from models.base import Base


class Rectangle(Base):
    """class rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """iniitialize method"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """getter for width"""
        return self.__width

    @property
    def height(self):
        """getter for height"""
        return self.__height

    @property
    def x(self):
        """getter forr x"""
        return self.__x

    @property
    def y(self):
        """getter fr y"""
        return self.__x

    @width.setter
    def width(self, value):
        """width setter"""

        self.__width = value

    @height.setter
    def height(self, value):
        """height setter"""
        self.__height = value

    @x.setter
    def x(self, value):
        """setter for x"""
        self.__x = value

    @y.setter
    def y(self, value):
        self.__y = value
