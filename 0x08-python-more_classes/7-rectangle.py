#!/usr/bin/python3
"""Define a class Rectangle"""


class Rectangle:
    """Represents a rectangle object"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle
        Args:
            width (int): width of the rectangle.
            height (int): height of the rectangle.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1
        print_symbol = Rectangle.print_symbol

    @property
    def width(self):
        """Getter and Setter for width attribute"""
        return (self.__width)

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter and Setter for height attribute"""
        return (self.__height)

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of the rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Returns the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return (2 * (self.__width + self.__height))

    def __repr__(self):
        """Creates a new instance using eval()"""
        return ("Rectangle(" + str(self.__width) + ", " +
                str(self.__height) + ")")

    def __str__(self):
        """Prints a rectangle with character '#'"""
        if self.__width == 0 or self.__height == 0:
            return ("")
        characters = []
        for i in range(self.__height):
            [characters.append(str(self.print_symbol))
                for j in range(self.__width)]
            if i < self.__height - 1:
                characters.append('\n')
        return ("".join(characters))

    def __del__(self):
        """Prints a goodbye message"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
