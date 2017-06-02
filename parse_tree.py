"""This program creates a parse tree out of a fully parenthesized expression."""


from data_structures.stack import Stack
from data_structures.binary_tree import BinaryTree


def build_parse_tree(exp):
    tokens = exp.split()
    operators = {"+", "-", "*", "/", "//", "%", "**"}
    tree = BinaryTree()
    node_stack = Stack()
    current_node = tree

    for token in tokens:
        if token == "(":
            current_node.left = BinaryTree()
            node_stack.push(current_node)
            current_node = current_node.left
        elif token == ")":
            current_node = node_stack.pop()
        elif token in operators:
            current_node.key = token
            current_node.right = BinaryTree
            node_stack.push(current_node)
            current_node = current_node.right
        else:
            current_node.key = token
            current_node = node_stack.pop()

    return tree
