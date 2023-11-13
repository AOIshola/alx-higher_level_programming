#!/usr/bin/python3
"""The test_rectangle Module"""


import unittest

class TestRectangleClass(unittest.TestCase):
    """Represents a Test Class"""
    def test_width_height(self):
        """width and height assigned"""
        self.assertEqual(Rectangle(2, 4)
