#!/usr/bin/python3
"""class base"""

import json


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
        
