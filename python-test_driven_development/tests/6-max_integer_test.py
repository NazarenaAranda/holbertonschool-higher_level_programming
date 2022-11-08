#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """tests"""
    def test_two_max(self):
        self.assertEqual(max_integer([8, 8, 3, 1, 2]), 8)

    def test_empty(self):
        self.assertEqual(max_integer([]), None)

    def test_negativ(self):
        self.assertEqual(max_integer([-5, -4, -2, -7, -1]), -1)

    def test_negativ_and_positiv(self):
        self.assertEqual(max_integer([-3, -2, -1, 1, 0, -8]), 1)

    def test_num_only(self):
        self.assertEqual(max_integer([7]), 7)

    def test_list_extensive(self):
        self.assertEqual(max_integer([1, 4, 6, 4, 2, 4, 6, 2, 8, 3, 1, 2, 1, 3, 2, 4, 98, 12, 43, 12, 223, 65, 1, 5, 13, 54, 7, 13]), 223)
