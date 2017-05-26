"""This program tests several different ways of creating lists.
By these results, I conclude that list creation methods can
be ordered by speed as follows (slowest first):

Concatenation (list += [i])
Appending     (list.append(i))
Comprehension (list = [x for x in range(n)])
Generator     (list = list(range(n)))

Interestingly, the addition of the profiling decorator function
added an extra tenth of a second to the run time of all methods
versus copying the timing code manually into each method.
"""


import time


def main():
    sf = "{} took {:.15f}"
    size = 10000000

    print(sf.format("Concatenation\t", concat(size)))
    print(sf.format("Append\t\t", append(size)))
    print(sf.format("Comprehension\t", comprehension(size)))
    print(sf.format("Generator\t", generator(size)))


def profiling(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        return time.time() - start
    return wrapper


@profiling
def concat(n):
    l = []
    for i in range(n):
        l += [n]


@profiling
def append(n):
    l = []
    for i in range(n):
        l.append(i)


@profiling
def comprehension(n):
    l = [x for x in range(n)]


@profiling
def generator(n):
    l = list(range(n))


if __name__ == "__main__":
    main()
