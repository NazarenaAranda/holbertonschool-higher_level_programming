#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """class TestMaxInteger"""
    def test0(self):
        with self.assertRaises(TypeError):
            max_integer(['naza', 6, 3, 7])

    def test1(self):
        self.assertEqual(max_integer([]), None)

    def test2(self):
        self.assertEqual(max_integer([7, 7, 7, 7, 7, 7]), 7)

    def test3(self):
        self.assertEqual(max_integer([-1, 6, 7, 3, -5, 51]), 51)

    def test4(self):
        self.assertEqual(max_integer([1, 6, 7, 3, 5, 51]), 51)

if __name__ == '__main__':
    unittest.main()
