#!/usr/bin/python3
"""The read_file module"""


def read_file(filename=""):
    """Reads a file and prints content"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
