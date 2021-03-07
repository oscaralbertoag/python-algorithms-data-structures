import unittest
import balanced_expression as be


class BalancedExpressionTest(unittest.TestCase):

    def test_balanced_expression(self):
        expected_and_input = [("", False), ("()", True), ("{}", True), ("[]", True), ("(", False), (")", False),
                              ("[", False), ("]", False), ("{", False), ("}", False), ("{[()]}", True),
                              ("({[]})", True), ("[({})]", True), ("(()()()())", True), ("[()()(){}]", True),
                              ("{{}()[]{}(()){{}}}", True), ("{{}()[]{}(()){{}}", False), ("((((()))))", True),
                              ("{{{{{}}}}}", True), ("[[[[[]]]]]", True), ("[[[]]", False), ("(()))", False),
                              ("(()()(()", False), ("{}}}}", False), ("{}()}}{{()}{()}}{(", False),
                              ("[[[[[]]]]](()()()()){{}()[]{}(()){{}}}({[{{{{{}}}}}]})", True)]

        for expression, expected in expected_and_input:
            self.assertEqual(expected, be.is_balanced(expression), f"Incorrect result for expression '{expression}'")
