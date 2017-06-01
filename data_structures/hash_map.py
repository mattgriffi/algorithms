"""This class implements a hash map."""


from data_structures.singly_linked_list import SinglyLinkedList


class Map:

    def __init__(self, size):
        """Creates a map with specified size. Note that size does not limit the number of
        key-value pairs that can be held in the map, but rather it controls the number of
        addresses available for hashing and storing keys. A larger size will reduce the odds
        of collisions, at the cost of initial memory usage."""
        self.size = size
        self.table = [None] * size

    def put(self, key, val):
        """Add a new key-value pair. If key already exists in map, its value will be
        overwritten."""

    def get(self, key):
        """Returns the value of give key, or None if key is not in the map."""

    def len(self):
        """Returns the number of key-value pairs in the map."""

    def __hash(self, key):
        """Returns the hash code for the given key."""

    def __delitem__(self, key):
        pass

    def __contains__(self, key):
        pass


class Pair:
    def __init__(self, key, value):
        self.key = key
        self.value = value