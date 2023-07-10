#!/usr/bin/python3
"""Square modue"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """inherted from rectangle"""

    def __init__(self, size):
        """init method"""
        self.integer_validator('size', size)
        self.__size = size
        super().__init__(self.__size, self.__size)
