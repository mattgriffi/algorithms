"""This class implements a min binary heap."""


class MinHeap:
    def __init__(self):
        self.heap = [0]
        self.current_size = 0

    def insert(self, k):
        """Adds new item k into the heap."""
        self.heap.append(k)
        self.current_size += 1
        self.__percolate_up()

    def find_min(self):
        """Returns the item with the minimum key value."""
        if self.current_size == 0:
            raise HeapException("cannot find min in an empty heap")
        return self.heap[1]

    def del_min(self):
        """Returns the item with the minimum key value and removes it from the heap."""
        if self.current_size == 0:
            raise HeapException("cannot del from an empty heap")
        min_item = self.heap[1]
        self.heap[1] = self.heap[-1]
        self.heap.pop()
        self.current_size -= 1
        self.__percolate_down(1)
        return min_item

    def is_empty(self):
        """Returns True if the heap is empty, else False."""
        return self.current_size == 0

    def size(self):
        """Returns the number of items currently in the heap."""
        return self.current_size

    def build_heap(self, key_list: list):
        """Builds a new heap from the keys in the key_list."""
        self.heap = [0] + key_list[:]
        self.current_size = len(key_list)
        i = self.current_size // 2
        while i > 0:
            self.__percolate_down(i)
            i -= 1

    def __percolate_up(self):
        """Takes the last item in the list and moves it up if needed."""
        c = p = self.current_size
        while p > 1:
            p //= 2
            if self.heap[c] < self.heap[p]:
                self.__swap(c, p)
                c = p
            else:
                break

    def __percolate_down(self, i):
        """Takes the given item in the list and moves down if needed."""
        while i * 2 <= self.current_size:
            min_child = self.__min_child(i)
            if self.heap[i] > self.heap[min_child]:
                self.__swap(i, min_child)
            i = min_child

    def __min_child(self, p):
        """Returns the index of the smallest child of the given parent node. If parent node is
        a leaf, returns the index of the left child slot. If parent node has only 1 child,
        returns the index of the left child slot."""
        if p * 2 + 1 > self.current_size:
            return p * 2
        elif self.heap[p * 2] < self.heap[p * 2 + 1]:
            return p * 2
        else:
            return p * 2 + 1

    def __swap(self, x, y):
        self.heap[x], self.heap[y] = self.heap[y], self.heap[x]


class HeapException(Exception):
    pass
