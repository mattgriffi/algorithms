"""This class implements an AVL tree, which is a subclass of BinarySearchTree."""


from data_structures.binary_search_tree import BinarySearchTree, Node


class AVLTree(BinarySearchTree):
    def __init__(self):
        super().__init__()

    def _put(self, key, value, current_node):
        """Recursively puts the key-value pair in the right place, and updates the balance
        factors."""
        if key == current_node.key:
            current_node.value = value
        elif key < current_node.key:
            if current_node.has_left_child():
                self._put(key, value, current_node.left)
            else:
                current_node.left = Node(key, value, parent=current_node)
                self.update_balance(current_node.left)
        else:
            if current_node.has_right_child():
                self._put(key, value, current_node)
            else:
                current_node.right = Node(key, value, parent=current_node)
                self.update_balance(current_node.right)

    def update_balance(self, node):
        """Recursively updates the balance factor of a node and its ancestors."""
        # If the node's balance factor is not between -1 and 1, rebalance the tree
        if abs(node.balance_factor) > 1:
            self.rebalance(node)
            return
        if not node.is_root():
            # If the node is a left child, increase balance factor of parent by 1
            if node.is_left_child():
                node.parent.balance_factor += 1
            # If the node is a right child, decrease balance factor of parent by 1
            else:
                node.parent.balance_factor -= 1
            # If parent balance factor is now not 0, recursively update its balance
            if node.parent.balance_factor != 0:
                self.update_balance(node.parent)
