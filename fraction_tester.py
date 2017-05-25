# This class tests all method of the Fraction class

import unittest
import random
from fraction import Fraction

class TestFractionMethods(unittest.TestCase):

    def setUp(self):
        self.nums = [random.randint(0, 999) for _ in range(1000)]
        self.denoms = [random.randint(0, 999) for _ in range(1000)]
        self.pairs = zip(self.nums, self.denoms)


    def test_str(self):
        """Test the __str__ method"""
        for n, d in self.pairs:
            frac = Fraction(n, d)
            correct = str(n) + "/" + str(d)
            self.assertEqual(
                    str(frac), correct,
                    "Fraction {} does not equal {}".format(
                        str(frac), correct
                     ))