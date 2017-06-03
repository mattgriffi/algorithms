"""Unit tests for binary heaps."""


import random
import unittest

from data_structures.binary_heap import MinHeap, HeapException


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

    def test_build_heap(self):
        keys = [random.randint(-100, 100) for _ in range(100)]
        self.h.build_heap(keys)
        sorted_keys = []
        while not self.h.is_empty():
            self.check_min(self.h)
            sorted_keys.append(self.h.del_min())
        self.assertTrue(sorted(keys) == sorted_keys)

    def test_heap_fuzzer(self):

        for _ in range(20):

            h = MinHeap()
            size = 0

            # Make sure it behaves properly after instantiation
            self.assertTrue(h.is_empty())
            with self.assertRaises(HeapException):
                h.find_min()
            with self.assertRaises(HeapException):
                h.del_min()
            self.assertEqual(size, h.size())

            # Set the bias toward insertion operations
            bias = random.uniform(0.45, 0.55)

            for _ in range(10000):

                self.assertEqual(size, h.size())

                # Do an insert operation
                if random.random() < bias:
                    h.insert(random.randint(-1000000, 1000000))
                    size += 1
                    self.check_min(h)
                # Make sure it behaves properly when empty
                elif size == 0:
                    self.assertTrue(h.is_empty())
                    with self.assertRaises(HeapException):
                        h.find_min()
                    with self.assertRaises(HeapException):
                        h.del_min()
                # Do find and del operations
                else:
                    self.assertEqual(h.find_min(), h.del_min())
                    size -= 1
                    if size > 0:
                        self.check_min(h)

    def check_min(self, heap):
        self.assertEqual(min(heap.heap[1:]), heap.heap[1], f"\n{heap.heap}")
        self.assertEqual(min(heap.heap[1:]), heap.find_min(), f"\n{heap.heap}")


if __name__ == "__main__":
    unittest.main()
