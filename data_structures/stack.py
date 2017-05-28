"""This class implements a LIFO Stack with the usual methods.

All operations in this stack are constant time.
"""


class Stack:

    def __init__(self):
        self.stack = []

    def push(self, item):
        """Pushes item onto stack."""
        self.stack.append(item)

    def pop(self):
        """Removes and return the top element of the stack.
        Raises a StackException if the stack is empty."""
        if not len(self.stack):
            raise StackException("cannot pop from an empty stack")
        return self.stack.pop()

    def peek(self):
        """Returns the top element of the stack, without removing it.
        Raises a StackException if the stack is empty."""
        if not len(self.stack):
            raise StackException("cannot peek at an empty stack")
        return self.stack[-1]

    def isEmpty(self) -> bool:
        """Returns True if the stack is empty, else False."""
        return len(self.stack) == 0

    def size(self) -> int:
        """Returns the number of elements currently in the stack"""
        return len(self.stack)


class StackException(Exception):
    pass
