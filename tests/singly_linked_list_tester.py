"""Unit tests for SinglyLinkedList."""

import random
import unittest

from data_structures.singly_linked_list import SinglyLinkedList, ListException


class SinglyLinkedListTester(unittest.TestCase):
    def setUp(self):
        self.li = SinglyLinkedList()

    def test_add_remove(self):
        self.assertTrue(self.li.isEmpty())
        with self.assertRaises(ListException):
            self.li.remove(5)
        self.li.add(3)
        self.assertFalse(self.li.isEmpty())
        self.li.add(4)
        self.li.add(5)
        self.li.remove(4)
        with self.assertRaises(ListException):
            self.li.remove(4)
        self.li.remove(3)
        with self.assertRaises(ListException):
            self.li.remove(3)
        self.li.remove(5)
        with self.assertRaises(ListException):
            self.li.remove(5)
        self.assertTrue(self.li.isEmpty())

    def test_pop(self):
        with self.assertRaises(ListException):
            self.li.pop(-5)
        with self.assertRaises(ListException):
            self.li.pop()
        for i in range(5):
            self.li.add(i)
        self.assertEqual(5, self.li.size())
        with self.assertRaises(ListException):
            self.li.pop(5)

        self.assertFalse(self.li.isEmpty())

        self.assertEqual(0, self.li.pop())
        self.assertEqual(4, self.li.size())

        self.assertEqual(1, self.li.pop())
        self.assertEqual(3, self.li.size())

        self.assertEqual(4, self.li.pop(0))
        self.assertEqual(2, self.li.size())

        self.assertEqual(2, self.li.pop(1))
        self.assertEqual(1, self.li.size())

        self.assertEqual(3, self.li.pop(0))
        self.assertEqual(0, self.li.size())
        self.assertTrue(self.li.isEmpty())

    def test_append(self):
        self.li.append(1)
        self.li.append(2)
        self.assertEqual(2, self.li.pop())
        self.assertEqual(1, self.li.pop())

    def test_search_index(self):
        sim = [5, 6, 1, 7, 3, 2, 4, 9, 8, 0]
        for e in sim:
            self.li.append(e)
        for i in range(50):
            rand = random.randint(0, len(sim) - 1)
            self.assertTrue(self.li.search(sim[rand]))
            self.assertEqual(rand, self.li.index(sim[rand]))

        while not self.li.isEmpty():
            self.li.pop()

        sim = [1, 2, 3, 4, 4, 5, 6]
        for e in sim:
            self.li.append(e)
        for e in sim:
            self.assertEqual(sim.index(e), self.li.index(e))

    def test_all(self):
        pass

    def test_fuzz(self):
        pass


if __name__ == "__main__":
    unittest.main()
