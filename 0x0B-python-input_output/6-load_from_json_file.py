#!/usr/bin/python3
"""The load_from  Module"""


import json


def load_from_json_file(filename):
    """Creates an object from a JSON file"""
    with open(filename, encoding="utf-8") as f:
        return (json.loads(f.read()))
