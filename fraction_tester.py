# This class tests all method of the Fraction class

import unittest
import random
from fraction import Fraction

class TestFractionMethods(unittest.TestCase):

    def test_str(self):
        """Test the __str__ method"""
        for _ in range(1000):
            num = random.randint(0, 999)
            denom = random.randint(0, 999)
            frac = Fraction(num, denom)
            correct = str(num) + "/" + str(denom)
            self.assertEqual(str(frac), correct,
                             "Fraction {} does not equal {}".format(
                                 str(frac), correct
                             ))