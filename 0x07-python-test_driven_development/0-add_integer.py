#!/usr/bin/python3
"""Module adds two integers"""


def add_integer(a, b=98):
    """
    Returns the addition of a and b.

    Parameters:
        a (int): The first integer
        b (int): The second integer

    Returns:
        a + b: The addition of a and b.
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
