# This class implements a representation of decimal fractions.

class Fraction:
    def __init__(self, numerator, denominator):
        if type(numerator) is not int or type(denominator) is not int:
            raise TypeError("numerator and denominator must be type 'int'")
        if denominator == 0:
            raise ZeroDivisionError
        self.num = numerator
        self.den = abs(denominator)
        if denominator < 0:
            self.num *= -1

    def __str__(self):
        return "{}/{}".format(self.num, self.den)

    def __float__(self):
        return self.num / self.den

    def __int__(self):
        return self.num // self.den

    def __bool__(self):
        return self.num != 0

    def __add__(self, other):
        new_num = self.num * other.den + self.den * other.num
        new_den = self.den * other.den
        return Fraction(new_num, new_den).reduced()

    def __eq__(self, other):
        """Checks equality; reduces both fractions first"""
        if type(other) is not type(self):
            return False
        other = other.reduced()
        this = self.reduced()
        return this.num == other.num == 0 or \
            (this.num == other.num and this.den == other.den)

    def reduced(self):
        """Returns new fraction, equal to this one reduced to lowest terms"""
        gcd = self.get_gcd(self.num, self.den)
        return Fraction(self.num // gcd, self.den // gcd)

    def reduce(self):
        """Reduces fraction to lowest terms in place"""
        gcd = self.get_gcd(self.num, self.den)
        self.num //= gcd
        self.den //= gcd

    def is_reduced(self):
        return self.num == 0 or \
               self.get_gcd(self.num, self.den) == 1

    @staticmethod
    def get_gcd(m, n):
        """Use Euclid's Algorithm to find the
        greatest common divisor of m and n"""
        while m % n:
            old_m, old_n = m, n
            m, n = old_n, old_m % old_n
        return n
