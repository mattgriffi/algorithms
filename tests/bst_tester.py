"""Unit tests for binary search tree."""


import random
import unittest

from data_structures.binary_search_tree import BinarySearchTree


class BinarySearchTreeTester(unittest.TestCase):

    def setUp(self):
        self.bst = BinarySearchTree()

    def test_put_get(self):
        self.assert_empty(self.bst)
        self.bst.put(5, "a")
        self.assertEqual("a", self.bst.get(5))
        self.bst.put(2, "b")
        self.bst.put(21, "c")
        self.bst.put(4, "d")
        self.assertEqual(4, self.bst.length())
        self.assertEqual(4, len(self.bst))
        self.assertEqual("d", self.bst.get(4))
        self.assertEqual("b", self.bst.get(2))
        self.assertEqual("c", self.bst.get(21))
        self.assertEqual("a", self.bst.get(5))
        self.assertIsNone(self.bst.get(3))
    
    def test_set_getitem(self):
        self.assert_empty(self.bst)
        self.bst[5] = "a"
        self.assertEqual("a", self.bst[5])
        self.bst[2] = "b"
        self.bst[21] = "c"
        self.bst[4] = "d"
        self.assertEqual(4, self.bst.length())
        self.assertEqual(4, len(self.bst))
        self.assertEqual("d", self.bst[4])
        self.assertEqual("b", self.bst[2])
        self.assertEqual("c", self.bst[21])
        self.assertEqual("a", self.bst[5])
        self.assertIsNone(self.bst[3])

    def assert_empty(self, bst):
        self.assertEqual(0, bst.length())
        self.assertEqual(0, len(bst))


if __name__ == "__main__":
    unittest.main()
