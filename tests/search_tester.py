"""Unit tests for search algorithms."""


import random
import unittest

from search_algorithms import sequential_search


class SearchTester(unittest.TestCase):

    def setUp(self):
        self.a = []
        self.b = [1]
        self.c = [1, 2, 3, 4]
        self.d = [1, 2, True, "hello"]

    def test_sequential_search(self):
        self.assertEqual(1 in self.a, sequential_search(self.a, 1))
        self.assertEqual(1 in self.b, sequential_search(self.b, 1))
        self.assertEqual(2 in self.b, sequential_search(self.b, 2))
        self.assertEqual(3 in self.c, sequential_search(self.c, 3))
        self.assertEqual(5 in self.c, sequential_search(self.c, 5))
        self.assertEqual(1 in self.d, sequential_search(self.d, 1))
        self.assertEqual(True in self.d, sequential_search(self.d, True))
        self.assertEqual("hello" in self.d, sequential_search(self.d, "hello"))
        self.assertEqual("hi" in self.d, sequential_search(self.d, "hi"))
        self.assertEqual(False in self.d, sequential_search(self.d, False))

    def test_binary_search(self):
        pass


if __name__ == "__main__":
    unittest.main()
