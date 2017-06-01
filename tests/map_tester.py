"""Unit tests for the Map class."""


import random
import unittest

from data_structures.hash_map import Map, MapException


class MapTester(unittest.TestCase):

    def setUp(self):
        self.m_small = Map(2)
        self.m_large = Map(1_000_000)
        self.m = Map(100)

    def test_put(self):
        self.m.put(3, 4)
        self.m.put(4, 5)
        self.m.put(5, 4)
        self.m.put(6, 4)
        self.m.put(7, 4)
        self.m.put(8, 4)
        self.m.put(3, 5)
        self.m.put(3, 5)
        self.m.put(0, 4)

        self.m.put("hello", 4)
        self.m.put("hello", "haha")
        self.m.put("sakljfaskfjh-as9f87", 4)
        self.m.put("a;sfjkd_P()F* _()*#", 4)

        with self.assertRaises(MapException):
            self.m.put(range(5), 23)
        with self.assertRaises(MapException):
            self.m.put(Map(10), 23)
        with self.assertRaises(MapException):
            self.m.put(random.random, 23)

    def test_get(self):
        self.m.put("a", 1)
        self.assertEqual(1, self.m.get("a"))
        self.m.put("a", 3)
        self.assertEqual(3, self.m.get("a"))
        self.assertEqual(3, self.m.get("a"))

        self.m.put("b", 1)
        self.m.put(2, 2)
        self.m.put(3, 3)
        self.m.put("e", 4)
        self.assertEqual(1, self.m.get("b"))
        self.assertEqual(2, self.m.get(2))
        self.assertEqual(3, self.m.get(3))
        self.assertEqual(4, self.m.get("e"))

        self.assertIsNone(self.m.get("alsjkdf"))
        self.assertIsNone(self.m.get(4))
        self.assertIsNone(self.m.get(0))

        with self.assertRaises(MapException):
            self.assertIsNone(self.m.get(None))
        with self.assertRaises(MapException):
            self.assertIsNone(self.m.get(range))

    def test_len(self):
        self.assertEqual(0, self.m.len())
        self.m.put(2, 3)
        self.assertEqual(1, self.m.len())
        self.m.put(3, 4)
        self.m.put(4, 5)
        self.assertEqual(3, self.m.len())
        self.m.put(4, 6)
        self.assertEqual(3, self.m.len())

    def test_contains(self):
        self.assertFalse(3 in self.m)
        self.assertFalse("hello" in self.m)
        self.m.put(3, 5)
        self.assertTrue(3 in self.m)
        self.m.put("ha", "lkjasfdlj")
        self.assertTrue("ha" in self.m)

    def test_set_get(self):
        self.m["a"] = 3
        self.assertEqual(3, self.m["a"])
        self.m["a"] = 4
        self.assertEqual(4, self.m["a"])
        self.assertIsNone(self.m["lkjasdf"])

        with self.assertRaises(MapException):
            _ = self.m[range]

    def test_del(self):
        self.m["a"] = 1
        self.assertEqual(1, self.m.len())
        del self.m["a"]
        self.assertIsNone(self.m["a"])
        self.assertEqual(0, self.m.len())


if __name__ == "__main__":
    unittest.main()
