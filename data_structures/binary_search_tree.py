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


class Node:
    def __init__(self, key, value, left=None, right=None, parent=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

    def is_left_child(self):
        """Returns True if node is the left child of its parent, else False."""
        return self.parent and self.parent.left == self

    def is_right_child(self):
        """Returns True if node is the right child of its parent, else False."""
        return self.parent and self.parent.right == self

    def is_root(self):
        """Returns True if node is the root, else False."""
        return self.parent is None

    def is_leaf(self):
        """Returns True if node has no children, else False."""
        return self.left is None and self.right is None

    def has_two_children(self):
        """Returns True if node has both a left and right child, else false."""
        return self.left is not None and self.right is not None

