"""This class implements a singly-linked list."""


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def add(self, item):
        """Adds item to the start of the list."""

    def remove(self, item):
        """Removes given item from the list."""

    def search(self, item):
        """Returns True if item is in the list, else False."""

    def isEmpty(self):
        """Returns True if the list is empty, else False."""

    def size(self):
        """Returns the number of items currently in the list."""

    def append(self, item):
        """Adds item to the end of the list."""

    def index(self, item):
        """Returns the index of the first occurrence of item in the list."""

    def insert(self, pos, item):
        """Inserts item at pos in the list, moving other items back."""

    def pop(self, pos=-1):
        """Returns item at given pos, and removes it from the list. Will return and remove
        the last item in the list by default."""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
