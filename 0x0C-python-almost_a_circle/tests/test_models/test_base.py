#!/usr/bin/python3
"""test base class"""
import unittest
from models.base import Base


class TestCase(unittest.TestCase):
    def test_base_id(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base()
        b3 = Base()
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)

        b4 = Base(12)
        b5 = Base()
        self.assertEqual(b4.id, 12)
        self.assertEqual(b5.id, 4)

if __name__ == '__main__':
    unittest.main()