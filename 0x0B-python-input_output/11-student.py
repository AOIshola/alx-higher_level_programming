#!/usr/bin/python3
"""The student JSON Module"""


class Student:
    """Represents a Student Object"""
    def __init__(self, first_name, last_name, age):
        """Initialize an instance of the class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Generate a JSON dictionary representation
        of class"""
        my_keys = {}
        if attrs is None:
            my_keys = ({attr: getattr(self, str(attr)) for attr in dir(self) if
                        not callable(getattr(self, attr)) and
                        not attr.startswith("__")})
        elif (type(attrs) == list and
                all(isinstance(attr, str) for attr in attrs)):
            for attr in attrs:
                if attr in dir(self):
                    my_keys[attr] = getattr(self, str(attr))
        return (my_keys)

    def reload_from_json(self, json):
        """Replaces all attributes of the student instance"""
        for key, val in json.items():
            if key in dir(self):
                vars(self)[key] = val
