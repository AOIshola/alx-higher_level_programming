#!/usr/bin/python3
"""Describes a MyList class"""


class MyList(list):
    """Represents a MyList object"""

    def print_sorted(self):
        """Prints a sorted list"""
        print(sorted(self))
