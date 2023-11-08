#!/usr/bin/python3
"""The to_json Module"""


import json


def to_json_string(my_obj):
    """Return the JSON representation of an object"""
    s = json.dumps(my_obj)
    return (s)
