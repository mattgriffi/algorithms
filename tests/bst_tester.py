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
        self.bst[2] = "e"
        self.assertEqual("e", self.bst[2])

    def test_contains(self):
        self.assertFalse(3 in self.bst)
        self.bst[3] = "a"
        self.assertTrue(3 in self.bst)
        self.bst[2] = None
        self.assertTrue(2 in self.bst)

    def test_delete(self):
        self.bst[99] = "a"
        del self.bst[99]
        self.bst[5] = "a"
        self.bst[2] = "b"
        self.bst[1] = "c"
        self.bst[4] = "d"
        self.assertEqual(4, self.bst.length())
        self.assertIsNone(self.bst[99])
        with self.assertRaises(KeyError):
            del self.bst[99]

        del self.bst[2]
        with self.assertRaises(KeyError):
            del self.bst[2]
        self.assertEqual("c", self.bst[1])
        self.assertEqual("d", self.bst[4])
        del self.bst[5]
        self.assertEqual("c", self.bst[1])
        self.assertEqual("d", self.bst[4])

    def assert_empty(self, bst):
        self.assertEqual(0, bst.length())
        self.assertEqual(0, len(bst))


if __name__ == "__main__":
    unittest.main()
