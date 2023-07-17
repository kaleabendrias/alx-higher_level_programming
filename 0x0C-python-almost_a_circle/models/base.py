#!/usr/bin/python3
"""class base"""

import json
import os
import csv


class Base:
    """handels the id"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initalize method"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""

        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        if (type(list_dictionaries) != list or
                not all(type(x) == dict for x in list_dictionaries)):
            raise TypeError("list_dictionaries must be a list of dictionaries")
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""

        if list_objs is None or list_objs == []:
            li = "[]"
        else:
            li = cls.to_json_string([o.to_dictionary() for o in list_objs])
        fi = cls.__name__ + ".json"
        with open(fi, 'w') as f:
            f.write(li)

    @staticmethod
    def from_json_string(json_string):
        """returns list of json string"""

        li = []
        if json_string is not None and json_string != '':
            if type(json_string) != str:
                raise TypeError("json_string must be a string")
            li = json.loads(json_string)
        return li

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with allattr set"""
        if cls.__name__ == 'Rectangle':
            n = cls(1, 1)
        elif cls.__name__ == 'Square':
            n = cls(1)
        n.update(**dictionary)
        return n

    @classmethod
    def load_from_file(cls):
        """returns li of insta"""
        fi = cls.__name__ + ".json"
        li = []
        lis_dic = []
        if os.path.exists(fi):
            with open(fi, 'r') as f:
                s = f.read()
                lis_dic = cls.from_json_string(s)
                for d in lis_dic:
                    li.append(cls.create(**d))
        return li

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """serilize in csv"""
        if (type(list_objs) != list and list_objs is not None or
                not all(isinstance(x, cls) for x in list_objs)):
            raise TypeError("list_objs must be a list of instances")

        fi = cls.__name__ + ".csv"
        with open(fi, 'w') as f:
            if list_objs is not None:
                list_objs = [x.to_dictionary() for x in list_objs]
                if cls.__name__ == 'Rectangle':
                    fields = ['id', 'width', 'height', 'x', 'y']
                elif cls.__name__ == 'Square':
                    fields = ['id', 'size', 'x', 'y']
                writer = csv.DictWriter(f, fieldnames=fields)
                writer.writeheader()
                writer.writerows(list_objs)

    @classmethod
    def load_from_file_csv(cls):
        """deserialize csv"""

        fi = cls.__name__ + ".csv"
        li = []
        if os.path.exists(fi):
            with open(fi, 'r') as f:
                reader = csv.reader(f, delimiter=',')
                if cls.__name__ == 'Rectangle':
                    fields = ['id', 'width', 'height', 'x', 'y']
                elif cls.__name__ == 'Square':
                    fields = ['id', 'size', 'x', 'y']
                for x, row in enumerate(reader):
                    if x > 0:
                        i = cls(1, 1)
                        for j, e in enumerate(row):
                            if e:
                                setattr(i, fields[j], int(e))
                        li.append(i)
        return li

    @staticmethod
    def draw(list_rectangles, list_squares):
        """draws rects and squares"""
        import turtle
        import time

        t = turtle.Turtle()
        t.color("black")
        turtle.bgcolor("white")
        t.shape("square")
        t.pensize(8)

        for i in (list_rectangles + list_squares):
            t.penup()
            t.setpos(0, 0)
            turtle.Screen().colormode(255)
            Base.draw_rect(t, i)
            time.sleep(1)
        time.sleep(5)

    @staticmethod
    def draw_rect(t, rect):
        """cont of draw"""

        t.penup()
        t.setpos(rect.x, rect.y)
        t.pendown()
        t.forward(rect.width)
        t.left(90)
        t.forward(rect.height)
        t.left(90)
        t.forward(rect.width)
        t.left(90)
        t.forward(rect.height)
