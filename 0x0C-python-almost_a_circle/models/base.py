#!/usr/bin/python3
"""The base module"""


import json
import os
import turtle



class Base:
    """Represents the base class"""
    __nb_objects = 0
    t = turtle.Turtle()
    t.color("blue", "blue")

    def __init__(self, id=None):
        """Initializes all Instances
        of the Base class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation
        of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return ("[]")
        return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation
        of list_objs to a file"""
        my_list = []
        filename = cls.__name__ + ".json"
        with open(filename, encoding="utf-8", mode="w") as f:
            if list_objs is None:
                f.write("[]")
            else:
                for obj in list_objs:
                    s = obj.to_dictionary()
                    my_list.append(s)
                s = Base.to_json_string(my_list)
                f.write(s)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string
        representation json_string"""
        if json_string is None or len(json_string) == 0:
            return ([])
        obj = json.loads(json_string)
        return (obj)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls(2)
        dummy.update(**dictionary)
        return (dummy)

    @classmethod
    def load_from_file(cls):
        """Load JSON from file"""
        my_list = []
        filename = cls.__name__ + ".json"
        if not os.path.exists(filename):
            return ([])
        with open(filename, encoding="utf-8") as f:
            s = f.read()
            my_objs = Base.from_json_string(s)
        for obj in my_objs:
            instance = cls.create(**obj)
            my_list.append(instance)
        return (my_list)

    @classmethod
    def load_from_file_csv(cls):
        """Load JSON from file"""
        my_list = []
        filename = cls.__name__ + ".csv"
        if not os.path.exists(filename):
            return ([])
        with open(filename, encoding="utf-8") as f:
            s = f.read()
            my_objs = Base.from_json_string(s)
        for obj in my_objs:
            instance = cls.create(**obj)
            my_list.append(instance)
        return (my_list)

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """writes the JSON string representation
        of list_objs to a file"""
        my_list = []
        filename = cls.__name__ + ".csv"
        with open(filename, encoding="utf-8", mode="w") as f:
            if list_objs is None:
                f.write("[]")
            else:
                for obj in list_objs:
                    s = obj.to_dictionary()
                    my_list.append(s)
                s = Base.to_json_string(my_list)
                f.write(s)

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw shapes using the turtle module"""
        for rect in list_rectangles:
            t.begin_fill()
            t.forward(rect.width)
            t.left(90)
            t.forward(rect.height)
            t.left(90)
            t.forward(rect.width)
            t.left(90)
            t.forward(rect.height)
            t.end_fill()
            t.pu()

        for sqr in list_squares:
            t.begin_fill()
            t.forward(sqr.width)
            t.left(90)
            t.fd(sqr.height)
            t.left(90)
            t.fd(sqr.width)
            t.left(90)
            t.forward(sqr.height)
            t.end_fill()

        turtle.done()
