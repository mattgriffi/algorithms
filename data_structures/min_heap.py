"""This class implements a min binary heap."""


class MinHeap:
    def __init__(self):
        self.heap = [0]

    def insert(self, k):
        """Adds new item k into the heap."""
        self.heap.append(k)
        self.__percolate_up()

    def find_min(self):
        """Returns the item with the minimum key value."""
        if len(self.heap) == 1:
            raise HeapException("cannot find min in an empty heap")
        return self.heap[1]

    def del_min(self):
        """Returns the item with the minimum key value and removes it from the heap."""
        if len(self.heap) == 1:
            raise HeapException("cannot del from an empty heap")
        min_item = self.heap[1]
        self.heap[1] = self.heap.pop()
        self.__percolate_down()
        return min_item

    def is_empty(self):
        """Returns True if the heap is empty, else False."""

    def size(self):
        """Returns the number of items currently in the heap."""

    def build_heap(self, key_list: list):
        """Builds a new heap from the keys in the key_list."""

    def __percolate_up(self):
        """Takes the last item in the list and moves it up if needed."""
        c = p = len(self.heap) - 1
        while p > 1:
            p //= 2
            if self.heap[c] < self.heap[p]:
                self.__swap(c, p)
                c = p
            else:
                break

    def __percolate_down(self):
        pass

    def __swap(self, x, y):
        self.heap[x], self.heap[y] = self.heap[y], self.heap[x]


class HeapException(Exception):
    pass
