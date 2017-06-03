"""This class implements a binary search tree that stores key-value pairs, sorted by key."""


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
        self.size += 1

    def _put(self, key, value, current_node: Node):
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

    def get(self, key):
        """Returns the value of key if it exists in the tree, else returns None."""
        if self.root is None:
            return None
        else:
            search_node = self._get(key, self.root)
            return search_node.value if search_node is not None else None

    def _get(self, key, current_node: Node):
        """Recursively gets the node with key."""
        # If current node matches the key, return it
        if key == current_node.key:
            return current_node
        # Else if key is less than current node, recursively go left
        elif key < current_node.key:
            if current_node.has_left_child():
                return self._get(key, current_node.left)
            else:
                return None
        # Else if key is greater than current node, recursively go right
        else:
            if current_node.has_right_child():
                return self._get(key, current_node.right)
            else:
                return None

    def delete(self, key):
        """Deletes the node of the given key from the tree. Raises a KeyError if key is not in
        the tree."""
        # Root is None
        if self.root is None:
            raise KeyError("cannot delete from empty tree")
        # Root is the only node and is the node to delete
        elif self.size == 1 and self.root.key == key:
            self.root = None
        # There are multiple nodes in the tree
        else:
            node = self._get(key, self.root)
            if node is None:
                raise KeyError(f"key not in tree: {key}")
            self._remove(node)

        self.size -= 1

    def _remove(self, node: Node):
        """Removes the given node from the tree."""

        # node is a leaf
        if node.is_leaf():
            if node.parent.left == node:
                node.parent.left = None
            else:
                node.parent.right = None

        # node has one child
        elif not node.has_two_children():
            # node is a left child
            if node.is_left_child():
                if node.has_left_child():
                    node.parent.left = node.left
                    node.left.parent = node.parent
                else:
                    node.parent.left = node.right
                    node.right.parent = node.parent
            # node is a right child:
            elif node.is_right_child:
                if node.has_left_child():
                    node.parent.right = node.left
                    node.left.parent = node.parent
                else:
                    node.parent.right = node.right
                    node.right.parent = node.parent
            # node is the root
            else:
                if node.has_left_child():
                    self.root = self.root.left
                    self.root.parent = None
                else:
                    self.root = self.root.right
                    self.root.parent = None

        # node has two children
        else:
            successor = node.find_successor()
            successor.splice_out()
            node.key = successor.key
            node.value = successor.value

    def __delitem__(self, key):
        self.delete(key)

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        self.put(key, value)

    def __contains__(self, key):
        if self.root is None:
            return False
        return self._get(key, self.root) is not None

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

    def find_min(self):
        """Returns the node with the smallest key in the subtree of which this node is the
        root."""
        current = self
        while current.has_left_child():
            current = current.left
        return current

    def splice_out(self):
        """Node removes itself from the tree."""
        if self.is_leaf():
            if self.is_left_child():
                self.parent.left = None
            else:
                self.parent.right = None
        else:
            if self.has_left_child():
                if self.is_left_child():
                    self.parent.left = self.left
                else:
                    self.parent.right = self.left
                self.left.parent = self.parent
            else:
                if self.is_left_child():
                    self.parent.left = self.right
                else:
                    self.parent.right = self.right
                self.right.parent = self.parent

    def find_successor(self):
        successor = None
        if self.has_right_child():
            successor = self.right.find_min()
        elif self.is_left_child():
            successor = self.parent
        elif self.is_right_child():
            self.parent.right = None
            successor = self.parent.find_successor()
            self.parent.right = self
        return successor
