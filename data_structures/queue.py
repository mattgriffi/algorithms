"""This class defines a FIFO queue."""


class Queue:

    def __init__(self):
        self.q = []
        self.qsize = 0
        self.front = 0

    def enqueue(self, item):
        """Adds item to the end of the queue."""
        self.q.append(item)
        self.qsize += 1

    def dequeue(self):
        """Returns element at the front of the queue and removes it from the queue."""
        if self.qsize == 0:
            raise QueueException("cannot dequeue from empty queue")
        e = self.q[self.front]
        self.front += 1
        self.qsize -= 1
        return e

    def isEmpty(self):
        """Returns True if there is nothing in the queue, else False."""
        return self.qsize == 0

    def size(self):
        """Returns the number of elements currently in the queue."""
        return self.qsize


class QueueException(Exception):
    pass
