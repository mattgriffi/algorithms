# This class tests all method of the Fraction class

import unittest
import random
from fraction import Fraction as F

class TestFractionMethods(unittest.TestCase):

    def setUp(self):
        self.nums = [random.randint(0, 999) for _ in range(10000)]
        self.denoms = [random.randint(1, 999) for _ in range(10000)]
        self.pairs = zip(self.nums, self.denoms)

    def test_float(self):
        for n, d in self.pairs:
            frac = F(n, d)
            frac_float = float(frac)
            correct = n / d
            self.assertAlmostEqual(frac_float, correct, places=10)

    def test_add(self):
        for n, d in self.pairs:
            num_add = random.randint(0, 999)
            den_add = random.randint(1, 999)
            correct = n / d + num_add / den_add
            frac1 = F(n, d)
            frac2 = F(num_add, den_add)
            result = frac1 + frac2
            self.assertTrue(result.is_reduced())
            self.assertAlmostEqual(float(result), correct, places=10)

    def test_int(self):
        for n, d in self.pairs:
            frac = F(n, d)
            frac_int = int(frac)
            correct = n // d
            self.assertEqual(frac_int, correct)

    def test_bool(self):
        for n, d in self.pairs:
            frac = F(n, d)
            self.assertTrue(bool(n) == bool(frac))

    def test_eq(self):
        for n, d in self.pairs:
            frac1 = F(n, d)
            frac2 = F(n, d)
            self.assertTrue(frac1 == frac2)
        frac1 = F(3, 5)
        frac2 = F(2, 9)
        self.assertFalse(frac1 == 3)
        self.assertFalse(frac1 == range(3))
        self.assertFalse(frac1 == frac2)
        self.assertTrue(F(0, 5) == F(0, 3))

    def test_reduce(self):
        frac1 = F(6, 8)
        frac1.reduced()
        self.assertTrue(frac1 == F(3, 4))

    def test_is_reduced(self):
        frac2 = F(2, 3)
        frac3 = F(0, 5)
        self.assertTrue(frac2.is_reduced())
        self.assertTrue(frac3.is_reduced())

if __name__ == "__main__":
    unittest.main()
