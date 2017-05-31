"""This program contains several functions that solve various problems recursively."""


def factorial(n):
    if n < 0:
        raise Exception
    if n <= 1:
        return 1
    return n * factorial(n - 1)