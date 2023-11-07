#!/usr/bin/python3
"""Creates a BaseGeometry class"""


class BaseGeometry:
    """Represents a BaseGeometry class"""
    def area(self):
        """Implements the area of Geometry"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates the values of a Geometry"""
        if type(value) != int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")


class Rectangle(BaseGeometry):
    """Represents a Rectangle Class"""
    def __init__(self, width, height):
        """Initializes a Rectangle object"""
        self.__width = width
        super().integer_validator("width", width)
        self.__height = height
        super().integer_validator("height", height)
