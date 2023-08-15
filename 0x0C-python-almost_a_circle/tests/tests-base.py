#!/usr/bin/python3
"""Class Base test cases"""


import unittest
from models.base import Base


class testBase(unittest.TestCase):
    def test_id(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base()
        self.assertEqual(b2.id, 2)

        b3 = Base()
        self.assertEqual(b3.id, 3)

        b4 = Base(78)
        self.assertEqual(b4.id, 78)


testBase()
