#!/usr/bin/python3
"""module sqaure"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """ a class sqaure which inherits from rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """intitlalize the moethod"""

        self.size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """string rep o sqauare clas"""

        n = f"{type(self).__name__} ({self.id}) {self.x}\
/{self.y} {self.__width}"
        return n
