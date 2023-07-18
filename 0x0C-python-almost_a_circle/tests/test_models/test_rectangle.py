#!/usr/bin/python3
"""test base class"""
import unittest
from models.rectangle import Rectangle

class RectangleTest(unittest.TestCase):

    def test_Rectangle(self):

        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 2)

        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)

if __name__ == '__main__':
    unittest.main()
