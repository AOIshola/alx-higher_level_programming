#!/usr/bin/python3
"""Creates a BaseGeometry class"""


class BaseGeometry:
    """Represents a BaseGeometry class"""
    def area(self):
        """Implements the area method"""
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
        """Initializes a Rectangle class"""
        BaseGeometry.integer_validator(self, "width", width)
        self.__width = width
        BaseGeometry.integer_validator(self, "height", height)
        self.__height = height

    def area(self):
        """Returns the area of a Rectangle"""
        return (self.__width * self.__height)

    def __str__(self):
        """Implements print() and str()"""
        return ("[Rectangle] " + str(self.__width) + "/" + str(self.__height))


class Square(Rectangle):
    """Represents a Square Class"""
    def __init__(self, size):
        """Initializes the Square class"""
        BaseGeometry.integer_validator(self, "size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Returns the area of a Square"""
        return (self.__size ** 2)

    def __str__(self):
        """Implements print() and str() for Square()"""
        return ("[" + type(self).__name__ + "] " +
                str(self.__size) + "/" + str(self.__size))
