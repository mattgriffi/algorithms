"""This class implements a singly-linked list."""


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def add(self, item):

        if self.head is None:
            self.head = Node(item)
        else:
            temp = Node(item)
            temp.next = self.head
            self.head = temp

        self.length += 1

    def remove(self, item):
        """Removes first occurrence of given item from the list. Raises ListException if
        list is empty or if item is not in the list. """

        # Empty list
        if self.head is None:
            raise ListException("cannot remove from empty list")

        # Item is at head
        if self.head.data == item:
            if self.head.next:
                self.head = self.head.next
            else:
                self.head = None
        # Item is not at head
        else:
            cursor = self.head
            prev = self.head
            while cursor is not None and cursor.data != item:
                prev = cursor
                cursor = cursor.next

            # Item was not found
            if cursor is None:
                raise ListException("cannot remove nonexistent item: {}".format(item))

            # Remove item
            prev.next = cursor.next

        self.length -= 1

    def search(self, item):
        """Returns True if item is in the list, else False."""

    def isEmpty(self):
        """Returns True if the list is empty, else False."""
        return self.head is None

    def size(self):
        """Returns the number of items currently in the list."""
        return self.length

    def append(self, item):
        """Adds item to the end of the list."""

    def index(self, item):
        """Returns the index of the first occurrence of item in the list."""

    def insert(self, pos, item):
        """Inserts item at pos in the list, moving other items back."""

    def pop(self, pos=-1):
        """Returns item at given pos, and removes it from the list. Will return and remove
        the last item in the list by default. pos must be non-negative. Raises ListException
        if list is empty or if pos is greater than current list size."""

        if self.head is None:
            raise ListException("cannot pop from empty list")
        if pos < -1:
            raise ListException("pos must be non-negative")
        if pos > self.length - 1:
            raise ListException("list index out of range")

        # Pop end of list by default
        if pos == -1:
            pos = self.length - 1

        # Popping head
        if pos == 0:
            data = self.head.data
            self.head = self.head.next
            self.length -= 1
            return data
        # Popping something other than head
        else:
            cursor = self.head
            prev = cursor
            for i in range(pos):
                prev = cursor
                cursor = cursor.next

            prev.next = cursor.next
            self.length -= 1
            return cursor.data

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class ListException(Exception):
    pass
