"""This class defines a FIFO queue."""


class Queue:

    def __init__(self):
        self.q = []
        self.qsize = 0
        self.front = 0