# This class implements a representation of decimal fractions.

class Fraction:

    def __init__(self, numerator, denominator):
        self.num = numerator
        self.den = denominator


    def __str__(self):
        return "{}/{}".format(self.num, self.den)

    def __add__(self, other):
        new_num = self.num * other.den + self.den * other.num
        new_den = self.den * other.den
        return Fraction(new_num, new_den)

    def __float__(self):
        return self.num / self.den