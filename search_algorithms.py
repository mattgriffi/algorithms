"""This program implements several numeric searching algorithms."""


def sequential_search(a: list, x) -> bool:
    """This function determines whether item x is in list a. It does so by checking every
    element in the list sequentially. Also known as "linear search."
    Time complexity of O(n)
    """
    i = 0
    while i < len(a):
        if a[i] == x:
            return True
        i += 1
    return False


def sorted_sequential_search(a: list, x) -> bool:
    """This version of sequential search assumes the list is already sorted. It will stop
    when it knows that it has passed the position where x ought to be.
    It is still O(n)

    Although it will stop sooner in the case where x is not in the list, it has to do twice
    as many comparisons in the process, so whether or not this is actually an improvement at
    all is debatable.
    """
    i = 0
    while i < len(a) and a[i] <= x:
        if a[i] == x:
            return True
        i += 1
    return False


def binary_search(a: list, x) -> bool:
    """This function implements binary search. List a must be sorted.
    O(log n)
    """
    if len(a) == 0:
        return False

    left = 0
    right = len(a) - 1
    mid = (left + right) // 2

    while left < right and a[mid] != x:
        if x > a[mid]:
            left = mid + 1
        elif x < a[mid]:
            right = mid - 1
        mid = (left + right) // 2
    return a[mid] == x


def binary_search_recursive(a: list, x) -> bool:
    if len(a) == 0:
        return False
    return __binary_search_recurse(a, x, 0, len(a) - 1)


def __binary_search_recurse(a: list, x, left, right) -> bool:
    mid = (left + right) // 2
    if a[mid] == x:
        return True
    elif left > right:
        return a[mid] == x
    elif x > a[mid]:
        return __binary_search_recurse(a, x, mid + 1, right)
    else:
        return __binary_search_recurse(a, x, left, mid - 1)
