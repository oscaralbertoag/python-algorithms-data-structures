import unittest
import longest_sequence as fls


class LongestSequenceTest(unittest.TestCase):

    def test_longest_sequence_is_found(self):
        test_cases = [([7, 8, 9, 1, 3, 4, 5, 6], [3, 4, 5, 6, 7, 8, 9]),
                      ([4, 6, 8, 12, 33, 34, 35, 29, 0, 99, 100, 101, 102, 103], [99, 100, 101, 102, 103]),
                      ([1, 13, 50, 2, 89, 100], [1, 2]),
                      ([1, 3, 67, 9], [])]
        for numbers, expected in test_cases:
            self.assertListEqual(fls.find_longest_sequence(numbers), expected)
