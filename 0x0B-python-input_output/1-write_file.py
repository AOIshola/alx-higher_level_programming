#!/usr/bin/python3
"""The write_file Module"""


def write_file(filename="", text=""):
    """Writes to a file"""
    with open(filename, encoding="utf-8", mode="w") as f:
        f.write(text)
    with open(filename, encoding="utf-8", mode="r") as f:
        num_chars = 0
        for line in f:
            for char in line:
                num_chars += 1
    return (num_chars)
