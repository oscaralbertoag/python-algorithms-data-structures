from unittest import TestCase
import fibonacci as f


class FibonacciTest(TestCase):

    def test_fibonacci(self):
        expected_and_inputs = [(0, 0), (1, 1), (1, 2), (2, 3), (3, 4), (5, 5), (8, 6), (13, 7), (21, 8)]

        for expected, n in expected_and_inputs:
            result = f.fibonacci(n)
            self.assertEqual(expected, result, f"Result: {result} does not match expected: {expected} for n={n}")

    def test_memoized_fibonacci(self):
        expected_and_inputs = [(0, 0), (1, 1), (1, 2), (2, 3), (3, 4), (5, 5), (8, 6), (13, 7), (21, 8),
                               (12586269025, 50)]

        for expected, n in expected_and_inputs:
            result = f.memoized_fibonacci(n, {})
            self.assertEqual(expected, result, f"Result: {result} does not match expected: {expected} for n={n}")
