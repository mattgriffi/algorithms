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

    def _hash(self, key):
        """Returns the hash code for the given key."""
        if type(key) == str:
            total = 0
            for c in key:
                total += ord(c)
            key = total
        elif type(key) == int:
            pass
        else:
            raise MapException(f"key must be of type str or int, not {type(key)}")
        # This hash function was created by putting random bitwise operators together
        # It is probably terrible
        return ~((key ^ (key * 7)) << 20) % self.size

    def __delitem__(self, key):
        pass

    def __contains__(self, key):
        pass


class Pair:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class MapException(Exception):
    pass
