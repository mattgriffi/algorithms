"""This class defines a FIFO queue."""


class Queue:

    def __init__(self):
        self.q = []
        self.qsize = 0
        self.front = 0

    def enqueue(self, item):
        """Adds item to the end of the queue."""
        pass

    def dequeue(self):
        """Returns element at the front of the queue and removes it from the queue."""
        pass

    def isEmpty(self):
        """Returns True if there is nothing in the queue, else False."""
        pass

    def size(self):
        """Returns the number of elements currently in the queue."""
        pass