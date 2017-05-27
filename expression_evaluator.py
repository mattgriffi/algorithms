"""This program evaluates a given mathematical expression.
The expression should be in either normal, infix order, or
in postfix order. All operands, operators, and parenthesis
should be space-separated.

Examples:
    Infix: ( A + B ) * C
    Postfix: A B + C *
"""


from data_structures.stack import Stack
from operators import Operators


def main():
    exp = "A * B + C * D"
    print(ExpressionEvaluator.infix_to_postfix(exp))


class ExpressionEvaluator:

    operators = {'+': Operators.add, '-': Operators.sub,
                 '*': Operators.mul, '/': Operators.div}

    @staticmethod
    def infix_to_postfix(exp):
        precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
        exp = exp.split()
        result = []
        opstack = Stack()

        for c in exp:
            if c not in precedence:
                result.append(c)
            elif opstack.isEmpty():
                opstack.push(c)
            elif precedence[opstack.peek()] >= precedence[c]:
                result.append(opstack.pop())
                opstack.push(c)
            else:
                opstack.push(c)
        while not opstack.isEmpty():
            result.append(opstack.pop())
        return ' '.join(result)


if __name__ == "__main__":
    main()
