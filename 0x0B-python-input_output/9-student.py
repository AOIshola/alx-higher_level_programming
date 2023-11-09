#!/usr/bin/python3
"""The student JSON Module"""


class Student:
    """Represents a Student Object"""
    def __init__(self, first_name, last_name, age):
        """Initialize an instance of the class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Generate a JSON dictionary representation
        of class"""
        my_keys = ({attr: getattr(self, str(attr)) for attr in dir(self) if
                    not callable(getattr(self, attr)) and
                    not attr.startswith("__")})
        return (my_keys)
