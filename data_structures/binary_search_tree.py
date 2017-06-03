"""This class implements a binary search tree."""


class BinarySearchTree:

    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        """Returns the number of nodes in the tree."""
        return self.size

    def put(self, key, value):
        """Adds the key-value pair to the tree."""
        if self.root is None:
            self.root = Node(key, value)
        else:
            self._put(key, value, self.root)

    def _put(self, key, value, current_node):
        """Recursively puts the key-value pair in the right place."""
        # If the key is already in the tree, change its value
        if key == current_node.key:
            current_node.value = value
        # Else if the key is less than the current node
        elif key < current_node.key:
            # If current node has a left child, recursively move to that child
            if current_node.has_left_child():
                self._put(key, value, current_node.left)
            # If current node has no left child, create node
            else:
                current_node.left = Node(key, value, parent=current_node)
        # Else if key is greater than the current node
        else:
            # If current node has a right child, recursively move to that child
            if current_node.has_right_child():
                self._put(key, value, current_node)
            # If current node has no right child, create node
            else:
                current_node.right = Node(key, value, parent=current_node)

    def __setitem__(self, key, value):
        self.put(key, value)

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()


class Node:
    def __init__(self, key, value, left_child=None, right_child=None, parent=None):
        self.key = key
        self.value = value
        self.left = left_child
        self.right = right_child
        self.parent = parent

    def has_left_child(self):
        """Returns True if node has a left child, else False."""
        return self.left is not None

    def has_right_child(self):
        """Returns True if node has a right child, else False."""
        return self.right is not None

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

    def replace_node_data(self, key, value, left_child, right_child):
        self.key = key
        self.value = value
        self.left = left_child
        self.right = right_child
        if self.has_left_child():
            self.left.parent = self
        if self.has_right_child():
            self.right.parent = self
