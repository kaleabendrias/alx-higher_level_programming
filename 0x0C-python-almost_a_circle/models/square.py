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
/{self.y} - {self.width}"
        return n

    @property
    def size(self):
        """getter for var size"""
        return self.width

    @size.setter
    def size(self, value):
        """sets sixe to value"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """updates attr"""

        if args is not None and len(args) != 0:
            if len(args) >= 1:
                if type(args[0]) != int and args[0] is not None:
                    raise TypeError("id must be an integer")
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    if type(value) != int and value is not None:
                        raise TypeError("id must be an integer")
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """returns dict rep of Square"""

        dictionary = {
                "id": self.id,
                "x": self.x,
                "size": self.size,
                "y": self.y
                }
        return dictionary
