#!/usr/bin/python3
"""Class Rectangle test cases"""


import unittest
from models.rectangle import Rectangle


class test_rectangle(unittest.TestCase):
    def test_id(self):
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 2)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 3)

        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)


    def test_width(self):
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.width, 10)


    def test_height(self):
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.height, 2)


    def test_x(self):
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.x, 0)

        r3 = Rectangle(10, 2, 4, 0, 12)
        self.assertEqual(r3.x, 4)


    def test_y(self):
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.y, 0)

        r3 = Rectangle(10, 2, 0, 7, 12)
        self.assertEqual(r3.y, 7)


 

test_rectangle()
