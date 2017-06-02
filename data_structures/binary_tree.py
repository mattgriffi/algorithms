"""This class implements a recursive binary tree."""


class BinaryTree:

    def __init__(self, root=None):
        self.key = root
        self.left = None
        self.right = None

    def insert_left(self, key):
        if self.left is None:
            self.left = BinaryTree(key)
        else:
            new = BinaryTree(key)
            new.left = self.left
            self.left = new

    def insert_right(self, key):
        if self.right is None:
            self.right = BinaryTree(key)
        else:
            new = BinaryTree(key)
            new.right = self.right
            self.right = new
