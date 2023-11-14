#!/usr/bin/python3
"""The Rectangle module"""


from models.base import Base
import json


class Rectangle(Base):
    """Represents a Rectangle Class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes a Rectangle Object"""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.width = width
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.height = height
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.x = x
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Getter for width attribute"""
        return (self.__width)

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter for height attribute"""
        return (self.__height)

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter for x attribute"""
        return (self.__x)

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter for y attribute"""
        return (self.__y)

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the area of a Rectangle"""
        return (self.__width * self.__height)

    def display(self):
        """Displays the Rectange with '#'
        character"""
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            for j in range(self.__x):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """Implements str() for the object
        [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        return ("[" + type(self).__name__ + "] " + "(" + str(self.id) + ") " +
                str(self.__x) + "/" + str(self.__y) + " - " +
                str(self.__width) + "/" + str(self.__height))

    def update(self, *args, **kwargs):
        """Update object using non-keyworded *args"""
        for i in range(len(args)):
            if i == 0:
                self.id = args[i]
            elif i == 1:
                self.__width = args[i]
            elif i == 2:
                self.__height = args[i]
            elif i == 3:
                self.__x = args[i]
            else:
                self.__y = args[i]
        if len(args) == 0 and kwargs is not None:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "width":
                    self.__width = value
                elif key == "height":
                    self.__height = value
                elif key == "x":
                    self.__x = value
                else:
                    self.__y = value

    def to_dictionary(self):
        """Convert to dictionary"""
        my_keys = ({attr: getattr(self, str(attr)) for attr in dir(self) if
                    not callable(getattr(self, attr)) and
                    not attr.startswith("__") and not attr.startswith("_")})
        return (my_keys)
