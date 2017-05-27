"""This program evaluates a given mathematical expression.
The expression should be in either normal, infix order, or
in postfix order. All operands, operators, and parentheses
should be space-separated.
"""


from data_structures.stack import Stack
from operators import Operators


def main():
    exp = "( 2 + 3 + 12 ) * 3"
    postfix = ExpressionEvaluator.infix_to_postfix(exp)
    print(ExpressionEvaluator.eval_postfix(postfix))


class ExpressionEvaluator:

    @staticmethod
    def infix_to_postfix(exp):
        """Converts an expression in infix order to an equivalent
        expression in postfix order.
        Example:
        A * B + C * D  ->  A B * C D * +
        """
        precedence = {'(': 0, '+': 1, '-': 1, '*': 2, '/': 2, '//': 2, '%': 2, '**': 3}
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

    @staticmethod
    def eval_postfix(exp):
        """Evaluates an expression in postfix order."""
        operators = {'+': Operators.add, '-': Operators.sub,
                     '*': Operators.mul, '/': Operators.div_true,
                     '//': Operators.div, '%': Operators.mod,
                     '**': Operators.exp}
        exp = exp.split()
        exp_stack = Stack()
        for e in exp:
            # If e is an operand, push to stack
            if e not in operators:
                exp_stack.push(e)
            # If e is an operator, get operator method from dictionary
            # and pass in the two most recent operands from the stack.
            # Push the result back onto the stack
            else:
                result = operators[e](float(exp_stack.pop()), float(exp_stack.pop()))
                exp_stack.push(result)

        # The last thing left on the stack is the final answer
        return exp_stack.pop()

    @staticmethod
    def eval_infix(exp):
        """Evaluates an expression in infix order."""
        postfix = ExpressionEvaluator.infix_to_postfix(exp)
        result = ExpressionEvaluator.eval_postfix(postfix)
        return result


if __name__ == "__main__":
    main()
