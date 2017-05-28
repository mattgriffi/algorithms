"""Unit tests for deque."""


import random
import unittest

from data_structures.deque import Deque, DequeException


class DequeTester(unittest.TestCase):

    def setUp(self):
        self.d = Deque()
        self.sim = []

    def test_deque(self):
        self.assertTrue(self.d.isEmpty())
        self.assertTrue(self.d.size() == 0)
        with self.assertRaises(DequeException):
            self.d.removeFront()
        with self.assertRaises(DequeException):
            self.d.removeRear()
        self.d.addFront(1)
        self.d.addRear(2)
        self.assertEqual(1, self.d.removeFront())
        self.assertEqual(2, self.d.removeRear())
        self.assertTrue(self.d.isEmpty())
        self.assertTrue(self.d.size() == 0)


    def test_fuzz(self):
        pass


if __name__ == "__main__":
    unittest.main()
