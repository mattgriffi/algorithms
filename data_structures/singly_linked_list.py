"""This class implements a singly-linked list."""


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def add(self, item):

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
            self.head = self.head.next
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

        cursor = self.head
        while cursor is not None and cursor.data != item:
            cursor = cursor.next

        return cursor is not None

    def isEmpty(self):
        """Returns True if the list is empty, else False."""
        return self.head is None

    def size(self):
        """Returns the number of items currently in the list."""
        return self.length

    def append(self, item):
        """Adds item to the end of the list."""

        temp = Node(item)

        # If list is empty, new item becomes head
        if self.head is None:
            self.head = temp
        # Go to the end of list and add the new item in
        else:
            cursor = self.head
            for i in range(self.length - 1):
                cursor = cursor.next
            cursor.next = temp

        self.length += 1

    def index(self, item):
        """Returns the index of the first occurrence of item in the list."""

        if self.head is None:
            raise ListException("cannot index an empty list")

        cursor = self.head
        index = 0
        while cursor is not None and cursor.data != item:
            index += 1
            cursor = cursor.next

        if self.head is None:
            raise ListException("item does not exist in list")

        return index

    def insert(self, pos, item):
        """Inserts item at pos in the list, moving other items back. Raises ListException if
        pos is not a valid list index."""

        if pos > self.length - 1 or pos < 0:
            raise ListException("list index out of range")

        temp = Node(item)

        if self.head is None:
            self.head = temp
        elif pos == 0:
            temp.next = self.head
            self.head = temp
        else:
            cursor = self.head
            for i in range(pos - 1):
                cursor = cursor.next
            temp.next = cursor.next
            cursor.next = temp

        self.length += 1

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
