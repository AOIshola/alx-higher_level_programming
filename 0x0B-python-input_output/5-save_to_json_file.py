#!/usr/bin/python3
"""The save_json Module"""


import json


def save_to_json_file(my_obj, filename):
    """Writes an Object to s text file"""
    with open(filename, encoding="utf-8", mode="w") as f:
        json.dump(my_obj, f)
