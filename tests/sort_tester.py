"""Unit tests for the sorting algorithms."""


import random
import time
import unittest

from sorting_algorithms import bubble_sort, selection_sort, insertion_sort, shell_sort, \
    merge_sort, quick_sort


class SortTester(unittest.TestCase):

    def setUp(self):
        self.a = []
        self.b = [1]
        self.c = [2, 1]
        self.cs = sorted(self.c)
        self.d = [3, 2, 1, 1, 2, 3, 5, 4, 3, 6, 8, 9]
        self.ds = sorted(self.d)
        self.e = [3, 5, 3, 7, 4, 2, 3, 2, 6, 8, 5]
        self.es = sorted(self.e)
        self.f = [random.randint(-1000, 10000) for _ in range(10000)]
        self.fs = sorted(self.f)
        self.random = []
        for _ in range(200):
            self.random.append([random.randint(-10, 10) for _ in range(20)])

    def sort_helper(self, func):
        self.assert_with_message(func, self.a)
        self.assert_with_message(func, self.b)
        self.assert_with_message(func, self.c)
        self.assert_with_message(func, self.d)
        self.assert_with_message(func, self.e)
        start = time.time()
        self.assert_with_message(func, self.f)
        print(f"Time taken by {func.__name__}: {time.time() - start}")

        for a in self.random:
            self.assert_with_message(func, a)

    def assert_with_message(self, func, a):
        correct = sorted(a)
        result = func(a)
        self.assertEqual(correct, result,
                         f"\nOriginal: {a}\nCorrect:  {correct}\nGiven:    {result}")

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
