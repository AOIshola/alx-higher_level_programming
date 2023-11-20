#!/usr/bin/python3
"""The test_rectangle Module"""


import unittest
from models.square import Square


class TestSquareClass(unittest.TestCase):
    """Represents a Test Class"""
    def test_width_height(self):
        """width and height assigned"""
        r = Square(2)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 2)

    def test_width_str(self):
        """width as string"""
        with self.assertRaises(TypeError):
            Square("2")

    def test_width_zero_or_neg(self):
        """width as zero"""
        with self.assertRaises(ValueError):
            Square(0)
        with self.assertRaises(ValueError):
            Square(-1)

    def test_width_iter(self):
        """width as list"""
        with self.assertRaises(TypeError):
            Square([], 4)
        with self.assertRaises(TypeError):
            Square((), 4)
        with self.assertRaises(TypeError):
            Square({}, 4)
#        with self.assertRaises(TypeError):
 #           Square(4)
        with self.assertRaises(TypeError):
            Square()
        with self.assertRaises(TypeError):
            Square(None, 4)

    def test_height_str(self):
        """height as str"""
        with self.assertRaises(TypeError):
            Square("4")

    def test_height_zero_or_neg(self):
        """height as zero or negative"""
        with self.assertRaises(ValueError):
            Square(-4)
        with self.assertRaises(ValueError):
            Square(0)

    def test_height_iter(self):
        """height as iterable"""
        with self.assertRaises(TypeError):
            Square([4])
        with self.assertRaises(TypeError):
            Square({4})
        with self.assertRaises(TypeError):
            Square((4,))
        with self.assertRaises(TypeError):
            Square(None)

    def test_x_correct(self):
        """x assigned correctly"""
        r = Square(2, 4)
        self.assertEqual(r.x, 4)

    def test_x_zero_or_negative(self):
        """x under zero"""
        with self.assertRaises(ValueError):
            Square(2, -1)

    def test_x_iter(self):
        """x as an iterable"""
        with self.assertRaises(TypeError):
            Square(2, 4, [3])
        with self.assertRaises(TypeError):
            Square(2, 4, {3})
        with self.assertRaises(TypeError):
            Square(2, 4, (3,))
        with self.assertRaises(TypeError):
            Square(2, 4, None)
        with self.assertRaises(TypeError):
            Square(2, 4, "3")

    def test_y_correct(self):
        """y assigned correctly"""
        r = Square(2, 4, 0, 0)
        self.assertEqual(r.y, 0)

    def test_y_negative(self):
        """y under zero"""
        with self.assertRaises(ValueError):
            Square(2, 4, -1)

    def test_y_type(self):
        """y wrong type"""
        with self.assertRaises(TypeError):
            Square(2, 4, [])
        with self.assertRaises(TypeError):
            Square(2, 4, ())
        with self.assertRaises(TypeError):
            Square(2, 4, {})
        with self.assertRaises(TypeError):
            Square(2, 4, None)
        with self.assertRaises(TypeError):
            Square(2, 4, "0")
