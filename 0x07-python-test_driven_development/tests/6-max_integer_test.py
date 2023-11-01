#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Class representing a unittest object"""
    def test_max(self):
        """Tests for equal outputs vs input"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer("abcd"), "d")
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([1.2, 3.2, 0.1, 4.5]), 4.5)
        self.assertEqual(max_integer((2, 3, 4)), 4)
        self.assertEqual(max_integer([4, 1, 2, 3]), 4)
        self.assertEqual(max_integer([1, 3, 5, 2, 0]), 5)
        self.assertEqual(max_integer([3]), 3)

    def test_no_arg(self):
        """Tests for correct output for empty arguments"""
        self.assertEqual(max_integer(), None)

    def test_exceptions(self):
        """Tests for exceptions raised"""
        with self.assertRaises(TypeError) as r:
            max_integer(5)
        with self.assertRaises(TypeError) as r:
            max_integer(None)
