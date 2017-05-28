"""This class implements a LIFO Stack with the usual methods.
Does not do any error handling.

All operations in this stack are constant time.
"""


class Stack:

    def __init__(self):
        self.stack = []
        self.s_size = 0

    def push(self, item):
        self.s_size += 1
        self.stack.append(item)

    def pop(self):
        if self.s_size == 0:
            raise StackException("cannot pop from an empty stack")
        self.s_size -= 1
        return self.stack.pop()

    def peek(self):
        if self.s_size == 0:
            raise StackException("cannot peek at an empty stack")
        return self.stack[-1]

    def isEmpty(self):
        return self.s_size == 0

    def size(self):
        return self.s_size


class StackException(Exception):
    pass
