"""This program contains several functions that solve various problems recursively."""


def factorial(n):
    if n < 0:
        raise Exception
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def reverse_list(a):
    if len(a) <= 1:
        return a
    return [a[-1]] + reverse_list(a[:-1])
