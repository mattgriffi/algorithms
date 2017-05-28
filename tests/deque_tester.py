"""Unit tests for deque."""


import random
import unittest

from data_structures.deque import Deque, DequeException


class DequeTester(unittest.TestCase):

    def setUp(self):
        self.d = Deque()

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

        for i in range(20):
            bias = random.uniform(0.45, 0.55)
            self.d = Deque()
            sim = []

            self.assertTrue(self.d.isEmpty())
            self.assertTrue(self.d.size() == 0)

            for j in range(100000):

                self.assertEqual(len(sim), self.d.size())

                if len(sim) == 0:
                    self.assertTrue(self.d.isEmpty())
                    self.assertTrue(self.d.size() == 0)
                    with self.assertRaises(DequeException):
                        self.d.removeFront()
                    with self.assertRaises(DequeException):
                        self.d.removeRear()

                if random.random() < bias:
                    e = random.randint(-1000000000, 1000000000)
                    if random.random() < 0.5:
                        self.d.addFront(e)
                        sim.insert(0, e)
                    else:
                        self.d.addRear(e)
                        sim.append(e)
                elif len(sim) != 0:
                    self.assertFalse(self.d.isEmpty())
                    if random.random() < 0.5:
                        self.assertEqual(sim.pop(0), self.d.removeFront())
                    else:
                        self.assertEqual(sim.pop(), self.d.removeRear())


if __name__ == "__main__":
    unittest.main()
