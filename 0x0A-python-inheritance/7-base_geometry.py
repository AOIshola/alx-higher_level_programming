#!/usr/bin/python3
"""Creates a BaseGeometry class"""


class BaseGeometry:
    """Represents a BaseGeometry class"""
    def area(self):
        """implements area of shape"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates the values of a Geometry"""
        if not isinstance(value, int):
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
