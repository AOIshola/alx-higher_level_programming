#!/usr/bin/python3

def is_kind_of_class(obj, a_class):
    """Checks if an object is an instance
    of a specified class"""
    if isinstance(obj, a_class):
        return (True)
    return (False)
