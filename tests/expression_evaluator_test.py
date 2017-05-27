"""Unit tests for the ExpressionEvaluator"""


import unittest

from expression_evaluator import ExpressionEvaluator


class ExpressionEvaluatorTester(unittest.TestCase):

    def setUp(self):
        a = "2 + 3 * 4"
        aa = 14
        ap = "2 3 4 * +"
        b = "2 ** 3"
        ba = 8
        bp = "2 3 **"
        c = "5 / 2 + 1"
        ca = 3.5
        cp = "5 2 / 1 +"
        d = " 2 + 3 ** 3"
        da = 29
        dp = "2 3 3 ** +"
        e = "5 * 3 ** ( 4 - 2 )"
        ea = 45
        ep = "5 3 4 2 - ** *"
        x = "( 2 + 3 ) / ( 7 - 4 ) ** 2"
        xa = (2 + 3) / (7 - 4) ** 2
        z = "10 + 3 * 5 / ( 16 - 4 )"
        za = 11.25
        self.infix_to_postfix_tests = {a: ap, b: bp, c: cp, d: dp, e: ep}
        self.eval_infix_tests = {a: aa, b: ba, c: ca, d: da, e: ea, x: xa, z: za}

    def test_infix_to_postfix(self):
        for test in self.infix_to_postfix_tests:
            self.assertEqual(
                ExpressionEvaluator.infix_to_postfix(test),
                self.infix_to_postfix_tests[test]
            )

    def test_eval_infix(self):
        for test in self.eval_infix_tests:
            self.assertAlmostEqual(
                ExpressionEvaluator.eval_infix(test),
                self.eval_infix_tests[test],
                msg=test
            )


if __name__ == "__main__":
    unittest.main()
