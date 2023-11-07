#!/usr/bin/python3
"""The inherits_from Module"""


def inherits_from(obj, a_class):
    """Checks the subclass of an object"""
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return (True)
    return (False)
