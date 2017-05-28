"""This class defines a FIFO queue. It achieves constant time enqueue and dequeue operations
using a built-in list. However, this comes at the cost of space and occasional wasted time
to trim the fat. This trade-off could be avoided by using a more appropriate data structure,
such as a doubly linked list. """


class Queue:

    def __init__(self):
        self.q = []
        self.qsize = 0
        self.front = 0

    def enqueue(self, item):
        """Adds item to the end of the queue."""
        self.q.append(item)
        self.qsize += 1
        # If the list has gotten significantly longer than it needs to be, cut off the excess
        if len(self.q) > self.qsize * 20:
            self.q = self.q[self.front:]
            self.front = 0

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
