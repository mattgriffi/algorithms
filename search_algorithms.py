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
