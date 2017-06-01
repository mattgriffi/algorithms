"""Unit tests for the sorting algorithms."""


import random
import unittest

from sorting_algorithms import bubble_sort, selection_sort, insertion_sort, shell_sort, \
    merge_sort, quick_sort


class SortTester(unittest.TestCase):

    def setUp(self):
        self.a = []
        self.b = [1]
        self.c = [2, 1]
        self.cs = self.c.sort()
        self.d = [3, 2, 1, 1, 2, 3, 5, 4, 3, 6, 8, 9]
        self.ds = self.d.sort()
        self.e = [3, 5, 3, 7, 4, 2, 3, 2, 6, 8, 5]
        self.es = self.e.sort()
        self.f = [random.randint(-1000, 1000) for _ in range(random.randint(990, 1010))]
        self.fs = self.f.sort()

    def sort_helper(self, func):
        self.assertEqual(self.a, func(self.a))
        self.assertEqual(self.b, func(self.b))
        self.assertEqual(self.cs, func(self.c))
        self.assertEqual(self.ds, func(self.d))
        self.assertEqual(self.es, func(self.e))
        self.assertEqual(self.fs, func(self.f))

    def test_bubble(self):
        self.sort_helper(bubble_sort)

    def test_selection(self):
        self.sort_helper(selection_sort)

    def test_insertion(self):
        self.sort_helper(insertion_sort)

    def test_shell(self):
        self.sort_helper(shell_sort)

    def test_merge(self):
        self.sort_helper(merge_sort)

    def test_quick(self):
        self.sort_helper(quick_sort)


if __name__ == "__main__":
    unittest.main()
