#!/usr/bin/python3

"""Unittests for max_integer"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
	""" write unittests"""

	def test_ordered_list(self):

		ordered = [1, 2, 3, 4]
		r = max_integer(ordered)
		self.assertEqual(r, 4)

	def test_unordered_list(self):

		unordered = [1, 2, 4, 3]
		r = max_integer(unordered)
		self.assertEqual(r, 4)

	def test_max_at_begginning(self):

		max_at_beginning = [4, 3, 2, 1]
		r = max_integer(max_at_beginning)
		self.assertEqual(r, 4)

	def test_empty_list(self):

		empty = []
		r = max_integer(empty)
		self.assertEqual(r, None)

	def test_one_element_list(self):

		one_element = [7]
		r = max_integer(one_element)
		self.assertEqual(r, 7)

	def test_floats(self):

		floats = [1.53, 6.33, -9.123, 15.2, 6.0]
		r = max_integer(floats)
		self.assertEqual(r, 15.2)

	def test_ints_and_floats(self):

		ints_and_floats = [1.53, 15.5, -9, 15, 6]
		r = max_integer(ints_and_floats)
		self.assertEqual(r, 15.5)

	def test_string(self):

		string = "Brennan"
		r = max_integer(string)
		self.assertEqual(r, 'r')

	def test_list_of_strings(self):

		strings = ["Brennan", "is", "my", "name"]
		r = max_integer(strings)
		self.assertEqual(r, "name")

	def test_empty_string(self):
		r = max_integer("")
		self.assertEqual(r, None)

if __name__ == '__main__':
	unittest.main()
