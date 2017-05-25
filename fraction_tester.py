# This class tests all method of the Fraction class

import unittest
import random
from fraction import Fraction

class TestFractionMethods(unittest.TestCase):

    def setUp(self):
        self.nums = [random.randint(0, 999) for _ in range(10000)]
        self.denoms = [random.randint(1, 999) for _ in range(10000)]
        self.pairs = zip(self.nums, self.denoms)

    def test_str(self):
        for n, d in self.pairs:
            frac = Fraction(n, d)
            correct = str(n) + "/" + str(d)
            self.assertEqual(str(frac), correct)

    def test_float(self):
        for n, d in self.pairs:
            frac = Fraction(n, d)
            frac_float = float(frac)
            correct = n / d
            self.assertAlmostEqual(frac_float, correct, places=10)

    def test_add(self):
        for n, d in self.pairs:
            num_add = random.randint(0, 999)
            den_add = random.randint(1, 999)
            correct = n / d + num_add / den_add
            frac1 = Fraction(n, d)
            frac2 = Fraction(num_add, den_add)
            result = frac1 + frac2
            self.assertAlmostEqual(float(result), correct, places=10)

    def test_int(self):
        for n, d in self.pairs:
            frac = Fraction(n, d)
            frac_int = int(frac)
            correct = n // d
            self.assertEqual(frac_int, correct)

    def test_bool(self):
        for n, d in self.pairs:
            frac = Fraction(n, d)
            self.assertTrue(bool(n) == bool(frac))

if __name__ == "__main__":
    unittest.main()
