#!/usr/bin/python3
"""The is_same_class Module"""


def is_same_class(obj, a_class):
    """Checks if the object is of an exact
    type"""
    if type(obj) == a_class:
        return (True)
    return (False)
