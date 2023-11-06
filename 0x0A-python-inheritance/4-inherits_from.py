#!/usr/bin/python3

def inherits_from(obj, a_class):
    """Checks the subclass of an object"""
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return (True)
    return (False)
