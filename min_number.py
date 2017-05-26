"""This program finds the smallest number in a list"""


import random
import time


def main():
    a = [random.randint(0, 100000) for _ in range(9999)]
    print("slow:\n\tanswer: {}\n\ttime: {:.15f}\n".format(*slow_min(a)))
    print("fast:\n\tanswer: {}\n\ttime: {:.15f}\n".format(*fast_min(a)))
    print("built-in:\n\tanswer: {}\n\ttime: {:.15f}\n".format(*built_in_min(a)))


def slow_min(n):
    start = time.time()
    if not n:
        return None
    smallest = n[0]
    for i in n:
        for j in n:
            if j < smallest:
                smallest = j
    return smallest, time.time() - start


def fast_min(n):
    start = time.time()
    if not n:
        return None
    smallest = n[0]
    for i in n:
        if i < smallest:
            smallest = i
    return smallest, time.time() - start


def built_in_min(n):
    start = time.time()
    if not n:
        return None
    return min(n), time.time() - start


if __name__ == "__main__":
    main()
