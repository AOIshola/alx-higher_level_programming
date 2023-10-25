#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """Represent any square."""

    def __init__(self, size=0):
        """Initialize a new Square.
        Args:
            size (int): The size of the square
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """Returns the current area of the Square"""
        return (self.__size * self.__size)
