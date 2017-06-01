"""This program implements various sorting algorithms."""


def bubble_sort(a: list):
    """Bubble Sort works by swapping items in place. Larger items move toward the end of the
    list, and it loops through the list repeatedly until every item is sorted. It is one of the
    least efficient (serious) sorting algorithms.
    O(n^2)
    """
    # Create a copy of the list
    b = a.copy()
    # Get the len of the list
    n = len(b)

    # While there is more than 1 item in the unsorted portion of the list
    while n > 1:
        # Loop through the pairs of items in the unsorted portion
        for i in range(n - 1):
            # If the left item in the pair is greater than the right
            if b[i] > b[i + 1]:
                # Swap them
                b[i], b[i + 1] = b[i + 1], b[i]
        # Mark the last item in the list as sorted
        n -= 1

    return b


def selection_sort(a: list):
    return a


def insertion_sort(a: list):
    return a


def shell_sort(a: list):
    return a


def merge_sort(a: list):
    return a


def quick_sort(a: list):
    return a
