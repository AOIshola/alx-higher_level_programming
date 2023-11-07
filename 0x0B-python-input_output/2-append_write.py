#!/usr/bin/python3
"""Appends to a file"""

def append_write(filename="", text=""):
    """Appends to a file"""
    with open(filename, encoding="utf-8", mode="a") as f:
        f.write(text)
    with open(filename, encoding="utf-8") as f:
        num_chars = 0
        for line in f:
            for char in line:
                num_chars += 1
    return (num_chars)
