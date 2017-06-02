"""This program creates a parse tree out of a fully parenthesized expression."""


from data_structures.stack import Stack
from data_structures.binary_tree import BinaryTree


def build_parse_tree(exp):

    tokens = exp.split()
    operators = {"+", "-", "*", "/", "//", "%", "**"}
    tree = BinaryTree()
    node_stack = Stack()
    current_node = tree

    node_stack.push(current_node)

    for token in tokens:
        # If "(", make a new node to the left and move to it
        if token == "(":
            current_node.insert_left()
            node_stack.push(current_node)
            current_node = current_node.left
        # If ")", move back to the parent node
        elif token == ")":
            current_node = node_stack.pop()
        # If operator, put operator in current node, make new node to the right, and move to it
        elif token in operators:
            current_node.key = token
            current_node.insert_right()
            node_stack.push(current_node)
            current_node = current_node.right
        # Otherwise it must be an integer, so convert to int, put in node, then move to parent
        else:
            current_node.key = int(token)
            current_node = node_stack.pop()

    return tree


def evaluate(parse_tree):
    operators = {"+": (lambda x, y: x + y), "-": (lambda x, y: x - y),
                 "*": (lambda x, y: x * y), "/": (lambda x, y: x / y),
                 "//": (lambda x, y: x // y), "%": (lambda x, y: x % y),
                 "**": (lambda x, y: x ** y)}

    if parse_tree.key not in operators:
        return parse_tree.key
    else:
        return operators[parse_tree.key](
                evaluate(parse_tree.left),
                evaluate(parse_tree.right)
        )

tree = build_parse_tree("( ( 10 + 5 ) * 3 )")
print(evaluate(tree))