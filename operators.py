"""This class defines some static methods for basic arithmetic operations."""


class Operators:

    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def sub(a, b):
        return a - b

    @staticmethod
    def mul(a, b):
        return a * b

    @staticmethod
    def div(a, b):
        if b == 0:
            raise ZeroDivisionError
        return a // b

    @staticmethod
    def div_true(a, b):
        if b == 0:
            raise ZeroDivisionError
        return a / b

    @staticmethod
    def mod(a, b):
        if b == 0:
            raise ZeroDivisionError
        return a % b

    @staticmethod
    def exp(a, b):
        return a ** b
