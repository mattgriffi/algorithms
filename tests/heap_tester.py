"""Unit tests for binary heaps."""


import random
import unittest

from data_structures.min_heap import MinHeap


class HeapTester(unittest.TestCase):
    def setUp(self):
        self.h = MinHeap()

    def test_insert(self):
        for _ in range(1000):
            self.h.insert(random.randint(-100, 100))
            self.check_min(self.h)

    def test_del_min(self):

        for _ in range(100):
            self.h.insert(random.randint(-100, 100))

        sorted_list = []
        for _ in range(99):
            min_item = self.h.del_min()
            self.check_min(self.h)
            sorted_list.append(min_item)
        self.assertTrue(sorted(sorted_list) == sorted_list)

    def check_min(self, heap):
        self.assertEqual(min(heap.heap[1:]), heap.heap[1], f"\n{heap.heap}")
        self.assertEqual(min(heap.heap[1:]), heap.find_min(), f"\n{heap.heap}")


if __name__ == "__main__":
    unittest.main()
