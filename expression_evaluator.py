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
    exp = "( A + B + C ) * D"
    print(ExpressionEvaluator.infix_to_postfix(exp))


class ExpressionEvaluator:

    operators = {'+': Operators.add, '-': Operators.sub,
                 '*': Operators.mul, '/': Operators.div}

    @staticmethod
    def infix_to_postfix(exp):
        """Converts an expression in infix order to an equivalent
        expression in postfix order.
        Example:
        A * B + C * D  ->  A B * C D * +
        """
        precedence = {'(': 0, '+': 1, '-': 1, '*': 2, '/': 2}
        exp = exp.split()
        result = []
        opstack = Stack()

        for e in exp:
            # If e is a closing parenthesis, pop the stack until we reach
            # the opening parenthesis and append all those operators to the result
            if e == ')':
                while opstack.peek() != '(':
                    result.append(opstack.pop())
                opstack.pop()
            # If e is not an operator, append to result
            elif e not in precedence:
                result.append(e)
            # If there's nothing already on the stack, push e
            elif opstack.isEmpty():
                opstack.push(e)
            # If the top operator on the stack is higher precedence than e,
            # append that operator to the result and push e.
            # Ignore opening parens
            elif precedence[opstack.peek()] >= precedence[e] and e != '(':
                result.append(opstack.pop())
                opstack.push(e)
            # Else, push e to stack
            else:
                opstack.push(e)
        # Append every operator left on the stack
        while not opstack.isEmpty():
            result.append(opstack.pop())

        return ' '.join(result)


if __name__ == "__main__":
    main()
