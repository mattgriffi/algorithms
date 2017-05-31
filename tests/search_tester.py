"""Unit tests for search algorithms."""


import random
import unittest

from search_algorithms import sequential_search, sorted_sequential_search, binary_search, \
binary_search_recursive


class SearchTester(unittest.TestCase):

    def setUp(self):
        self.a = []
        self.b = [1]
        self.c = [0, 1, 2, 3, 4]
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

    def test_sorted_sequential_search(self):
        self.assertEqual(1 in self.a, sorted_sequential_search(self.a, 1))
        self.assertEqual(1 in self.b, sorted_sequential_search(self.b, 1))
        self.assertEqual(2 in self.b, sorted_sequential_search(self.b, 2))
        self.assertEqual(1 in self.c, sorted_sequential_search(self.c, 1))
        self.assertEqual(2 in self.c, sorted_sequential_search(self.c, 2))
        self.assertEqual(3 in self.c, sorted_sequential_search(self.c, 3))
        self.assertEqual(4 in self.c, sorted_sequential_search(self.c, 4))
        self.assertEqual(5 in self.c, sorted_sequential_search(self.c, 5))

    def test_binary_search(self):
        self.assertEqual(1 in self.a, binary_search(self.a, 1))
        self.assertEqual(1 in self.b, binary_search(self.b, 1))
        self.assertEqual(2 in self.b, binary_search(self.b, 2))
        self.assertEqual(1 in self.c, binary_search(self.c, 1))
        self.assertEqual(2 in self.c, binary_search(self.c, 2))
        self.assertEqual(3 in self.c, binary_search(self.c, 3))
        self.assertEqual(4 in self.c, binary_search(self.c, 4))
        self.assertEqual(5 in self.c, binary_search(self.c, 5))
        self.assertEqual(6 in self.c, binary_search(self.c, 6))
        self.assertEqual(0 in self.c, binary_search(self.c, 0))
        self.assertEqual(-1 in self.c, binary_search(self.c, -1))
        
    def test_recursive_binary_search(self):
        self.assertEqual(1 in self.a, binary_search_recursive(self.a, 1))
        self.assertEqual(1 in self.b, binary_search_recursive(self.b, 1))
        self.assertEqual(2 in self.b, binary_search_recursive(self.b, 2))
        self.assertEqual(1 in self.c, binary_search_recursive(self.c, 1))
        self.assertEqual(2 in self.c, binary_search_recursive(self.c, 2))
        self.assertEqual(3 in self.c, binary_search_recursive(self.c, 3))
        self.assertEqual(4 in self.c, binary_search_recursive(self.c, 4))
        self.assertEqual(5 in self.c, binary_search_recursive(self.c, 5))
        self.assertEqual(6 in self.c, binary_search_recursive(self.c, 6))
        self.assertEqual(0 in self.c, binary_search_recursive(self.c, 0))
        self.assertEqual(-1 in self.c, binary_search_recursive(self.c, -1))

    def test_binary_search_fuzz(self):

        for _ in range(20):

            a = [random.randint(-100, 100) for _ in range(100)]
            a.sort()

            for e in a:
                self.assertEqual(e in a, binary_search(a, e))
            for _ in range(10000):
                i = random.randint(-100, 100)
                self.assertEqual(i in a, binary_search(a, i))


if __name__ == "__main__":
    unittest.main()
