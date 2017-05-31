"""Tester for various recursive methods."""


import random
import unittest

from recursive_practice import factorial


class RecursiveTester(unittest.TestCase):

    def setUp(self):
        pass

    def test_factorial(self):
        with self.assertRaises(Exception):
            factorial(-1)
        self.assertEqual(1, factorial(0))
        self.assertEqual(1, factorial(1))
        self.assertEqual(2, factorial(2))
        self.assertEqual(6, factorial(3))
        self.assertEqual(24, factorial(4))
        self.assertEqual(120, factorial(5))
        self.assertEqual(720, factorial(6))
        self.assertEqual(5040, factorial(7))
        self.assertEqual(265252859812191058636308480000000, factorial(30))


if __name__ == "__main__":
    unittest.main()
