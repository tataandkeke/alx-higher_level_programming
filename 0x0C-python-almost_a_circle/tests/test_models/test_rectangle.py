#!/usr/bin/python3
""" Test Rectangle Module
"""


import os
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def test_rect(self):
        r = Rectangle(10, 10)
        self.assertEqual(r.id, 1)

    def test_rect2(self):
        r = Rectangle(1, 5)
        self.assertEqual(r.id, 2)

    def test_rect3(self):
        r = Rectangle(11, 15, 0, 0, 12)
        self.assertEqual(r.id, 12)

    def test_no_param(self):
        with self.assertRaises(TypeError):
            r2 = Rectangle()

    def test_1_param(self):
        with self.assertRaises(TypeError):
            r2 = Rectangle(3)

    def test_rect_from_base(self):
        self.assertIsInstance(Rectangle(4, 5), Base)

    def test_x(self):
        r2 = Rectangle(4, 5)
        self.assertEqual(r2.x, 0)

    def test_x_2(self):
        r2 = Rectangle(4, 5, 5)
        self.assertEqual(r2.x, 5)

    def test_y(self):
        r2 = Rectangle(4, 5)
        self.assertEqual(r2.y, 0)

    def test_y_2(self):
        r2 = Rectangle(4, 5, 7, 8)
        self.assertEqual(r2.y, 8)

    def test_all_param(self):
        r2 = Rectangle(4, 5, 7, 8, 9)
        self.assertEqual(9, r2.id)

    def test_width_private(self):
        r2 = Rectangle(4, 5, 7, 8, 9)
        with self.assertRaises(AttributeError):
            r2.__width

    def test_height_private(self):
        r2 = Rectangle(4, 5, 7, 8, 9)
        with self.assertRaises(AttributeError):
            r2.__height

    def test_x_private(self):
        r2 = Rectangle(4, 5, 7, 8, 9)
        with self.assertRaises(AttributeError):
            r2.__x

    def test_y_private(self):
        r2 = Rectangle(4, 5, 7, 8, 9)
        with self.assertRaises(AttributeError):
            r2.__y

if __name__ == "__main__":
    unittest.main()
