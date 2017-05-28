"""Unit tests for Queue."""

import random
import unittest

from data_structures.queue import Queue


class QueueTester(unittest.TestCase):

    def setUp(self):
        self.q = Queue()
        self.sim = []

    def test_queue(self):
        self.assertTrue(self.q.isEmpty())
        self.assertEqual(0, self.q.size())
        self.q.enqueue(5)
        self.assertFalse(self.q.isEmpty())
        self.assertEqual(1, self.q.size())
        self.assertEqual(5, self.q.dequeue())
        self.assertTrue(self.q.isEmpty())
        self.assertEqual(0, self.q.size())

    def test_fuzz(self):
        # Run the test 20 times with different biases toward enqueue and dequeue operations
        for i in range(20):
            bias = random.uniform(0.4, 0.6)
            # For each test, enqueue or dequeue many times
            # Compare outputs against simulated queue
            for j in range(100000):
                r = random.random()
                self.assertEqual(len(self.sim), self.q.size())
                if r < bias:
                    e = random.randint(-1000000, 1000000)
                    self.q.enqueue(e)
                    self.sim.append(e)
                elif len(self.sim):
                    self.assertFalse(self.q.isEmpty())
                    self.assertEqual(self.sim.pop(0), self.q.dequeue())


if __name__ == "__main__":
    unittest.main()
