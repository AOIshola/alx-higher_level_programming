#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """Represent any square."""

    def __init__(self, size=0):
        """Initialize a new Square.
        Args:
            size (int): The size of the square
        """
        self.size = size

    @property
    def size(self):
        """Getter and Setter for size attribute"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """Returns the current area of the Square"""
        return (self.__size * self.__size)

    def my_print(self):
        """Prints the square with the character #"""
        if self.__size == 0:
            print()
        for i in range(self.__size):
            for i in range(self.__size):
                print("#", end="")
            print()
