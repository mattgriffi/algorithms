"""This class implements a hash map. It uses the chaining method to handle collisions."""


class Map:

    def __init__(self, size):
        """Creates a map with specified size. Note that size does not limit the number of
        key-value pairs that can be held in the map, but rather it controls the number of
        addresses available for hashing and storing keys. A larger size will reduce the odds
        of collisions and increase speed at the cost of initial memory usage."""

        if size <= 0:
            raise MapException("size must be greater than 0")

        self.size = size
        self.table = [None] * size
        self.num_pairs = 0

    def put(self, key, val):
        """Add a new key-value pair. If key already exists in map, its value will be
        overwritten."""
        key_hash = self._hash(key)
        position = self.table[key_hash]
        # If that position in the table is empty
        if not position:
            # Add a new list with the new key-value pair
            self.table[key_hash] = [Pair(key, val)]
            self.num_pairs += 1
        # If there is already a list at that position
        else:
            already_exists = False
            # Update value of key if it already exists
            for pair in position:
                if pair.key == key:
                    pair.value = val
                    already_exists = True
                    break
            # Otherwise, add the key-value pair
            if not already_exists:
                position.append(Pair(key, val))
                self.num_pairs += 1

    def get(self, key):
        """Returns the value of give key, or None if key is not in the map."""
        key_hash = self._hash(key)
        value = None
        # Get the list at the hashed position of the table
        position = self.table[key_hash]
        # If there is anything at that position
        if position:
            for pair in position:
                if pair.key == key:
                    value = pair.value

        return value

    def len(self):
        """Returns the number of key-value pairs in the map."""
        return self.num_pairs

    def _hash(self, key):
        """Returns the hash code for the given key."""

        if type(key) is str:
            total = 0
            for c in key:
                total += ord(c)
            key = total

        elif type(key) is not int:
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
