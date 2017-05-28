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
        self.li.append(3)
        self.assertEqual(3, self.li.pop())
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

    def test_insert(self):
        for i in range(5):
            self.li.append(i)

        self.li.insert(0, 20)
        self.li.insert(2, 21)
        self.li.insert(6, 22)
        self.assertEqual(0, self.li.index(20))
        self.assertEqual(1, self.li.index(0))
        self.assertEqual(2, self.li.index(21))
        self.assertEqual(6, self.li.index(22))
        self.li.insert(4, 23)
        self.assertEqual(8, self.li.index(4))

    def test_fuzz(self):

        for i in range(20):

            bias = random.uniform(0.45, 0.55)
            li = SinglyLinkedList()
            sim = []

            self.assertTrue(li.isEmpty())
            self.assertEqual(0, li.size())

            for j in range(1000):

                self.assertEqual(len(sim), li.size())

                if len(sim) == 0:
                    self.assertTrue(li.isEmpty())
                    with self.assertRaises(ListException):
                        self.li.pop()
                    with self.assertRaises(ListException):
                        self.li.pop(5)
                    with self.assertRaises(ListException):
                        self.li.remove(5)
                    with self.assertRaises(ListException):
                        self.li.index(5)
                    with self.assertRaises(ListException):
                        self.li.insert(1, 1)

                # Insertion operations
                if random.random() < bias:
                    r = random.random()
                    pos = random.randint(0, len(sim)*2)
                    e = random.randint(-1000000000, 1000000000)

                    # Test add
                    if r < 0.33:
                        li.add(e)
                        sim.insert(0, e)
                    # Test append
                    elif r < 0.66:
                        li.append(e)
                        sim.append(e)
                    # Test insert to a random index
                    else:
                        if pos < len(sim):
                            li.insert(pos, e)
                            sim.insert(pos, e)
                        else:
                            with self.assertRaises(ListException):
                                li.insert(pos, e)

                # Removal operations
                elif not li.isEmpty():
                    r = random.random()
                    item = sim[random.randint(0, len(sim) - 1)]

                    # Test remove
                    if r < 0.33:
                        li.remove(item)
                        sim.remove(item)
                    # Test pop at end
                    elif r < 0.66:
                        self.assertEqual(sim.pop(), li.pop())
                    # Test pop at random index
                    else:
                        pos = random.randint(0, len(sim)*2)
                        if pos < len(sim):
                            self.assertEqual(sim.pop(pos), li.pop(pos))
                        else:
                            with self.assertRaises(ListException):
                                li.pop(pos)

                # Test search and index
                if random.random() < 0.1:

                    if len(sim) > 0:
                        index = random.randint(0, len(sim) - 1)
                        e = sim[index]
                        self.assertEqual(sim.index(e), li.index(e))
                        self.assertEqual(e in sim, li.search(e))

                    r = random.randint(-1000000000, 1000000000)
                    if r not in sim:
                        self.assertFalse(li.search(r))
                        with self.assertRaises(ListException):
                            self.li.index(r)

if __name__ == "__main__":
    unittest.main()
