"""This class defines some static methods for basic arithmetic operations."""


class Operators:

    @staticmethod
    def add(a, b):
        """a + b"""
        return a + b

    @staticmethod
    def sub(a, b):
        """a - b"""
        return a - b

    @staticmethod
    def mul(a, b):
        """a * b"""
        return a * b

    @staticmethod
    def div(a, b):
        """a // b
        Raises ZeroDivisionError if b is 0.
        For floating point division, use div_true."""
        if b == 0:
            raise ZeroDivisionError("integer division by zero ({} // {})".format(a, b))
        return a // b

    @staticmethod
    def div_true(a, b):
        """a / b
        Raises ZeroDivisionError if b is 0.
        For integer division, use div."""
        if b == 0:
            raise ZeroDivisionError("division by zero ({} / {})".format(a, b))
        return a / b

    @staticmethod
    def mod(a, b):
        """a % b
        Raises ZeroDivisionError if b is 0."""
        if b == 0:
            raise ZeroDivisionError("modulo by zero ({} % {})".format(a, b))
        return a % b

    @staticmethod
    def exp(a, b):
        """a ** b"""
        return a ** b
