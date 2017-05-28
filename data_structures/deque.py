"""This class implements a deque with the usual methods. Adding and removing from the rear are
O(1), while adding and removing from the front are O(n)."""


class Deque:
    def __init__(self):
        self.q = []

    def addFront(self, item):
        """Adds item to the front of the deque."""
        self.q.insert(0, item)

    def addRear(self, item):
        """Adds item to the rear of the deque."""
        self.q.append(item)

    def removeFront(self):
        """Returns element at the front of the deque and removes it."""
        if len(self.q) == 0:
            raise DequeException("cannot remove from empty deque")
        return self.q.remove(0)

    def removeRear(self):
        """Returns element at the rear of the deque and removes it."""
        if len(self.q) == 0:
            raise DequeException("cannot remove from empty deque")
        return self.q.pop()

    def isEmpty(self):
        """Returns True if deque is empty, else False."""
        return len(self.q) == 0

    def size(self):
        return len(self.q)


class DequeException(Exception):
    pass
