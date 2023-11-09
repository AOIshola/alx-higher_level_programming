#!/usr/bin/python3
"""The class_to_json Module"""


def class_to_json(obj):
    """Turns class to JSON"""
    my_keys = ({attr: getattr(obj, str(attr)) for attr in dir(obj) if
                not callable(getattr(obj, attr)) and
                not attr.startswith("__")})
    return (my_keys)
