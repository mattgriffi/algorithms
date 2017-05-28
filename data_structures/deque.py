"""This class implements a deque with the usual methods. Adding and removing from the rear are
O(1), while adding and removing from the front are O(n). Getting both sides to O(1) would
require a doubly linked list, or a fixed-size array."""


class Deque:
    def __init__(self):
        self.items = []

    def addFront(self, item):
        """Adds item to the front of the deque."""
        self.items.insert(0, item)

    def addRear(self, item):
        """Adds item to the rear of the deque."""
        self.items.append(item)

    def removeFront(self):
        """Returns element at the front of the deque and removes it."""
        if len(self.items) == 0:
            raise DequeException("cannot remove from empty deque")
        return self.items.pop(0)

    def removeRear(self):
        """Returns element at the rear of the deque and removes it."""
        if len(self.items) == 0:
            raise DequeException("cannot remove from empty deque")
        return self.items.pop()

    def isEmpty(self):
        """Returns True if deque is empty, else False."""
        return len(self.items) == 0

    def size(self):
        return len(self.items)


class DequeException(Exception):
    pass
