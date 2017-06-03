"""This class implements a binary search tree."""


class BinarySearchTree:

    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        """Returns the number of nodes in the tree."""
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()
