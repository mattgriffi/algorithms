# This class implements a representation of decimal fractions.

class Fraction:

    def __init__(self, numerator, denominator):
        self.num = numerator
        self.den = denominator


    def __str__(self):
        return "{}/{}".format(self.num, self.den)