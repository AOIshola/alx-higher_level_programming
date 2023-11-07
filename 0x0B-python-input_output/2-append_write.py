#!/usr/bin/python3
"""Appends to a file"""

def append_write(filename="", text=""):
    """Appends to a file"""
    with open(filename, encoding="utf-8", mode="a") as f:
        return (f.write(text))
