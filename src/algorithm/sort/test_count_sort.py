from unittest import TestCase
import count_sort as cs


class CountSortTest(TestCase):

    def test_count_sort(self):
        expected_and_inputs = [([], [], 0), ([3], [3], 1), ([1, 2, 3, 4, 5], [3, 4, 2, 1, 5], 10),
                               ([1, 35, 66, 120, 200], [120, 1, 35, 200, 66], 250),
                               ([100, 200, 300, 400, 500, 600, 700, 800, 900],
                                [100, 200, 300, 400, 500, 600, 700, 800, 900], 901),
                               ([100, 200, 300, 400, 500, 600, 700, 800, 900],
                                [100, 200, 900, 400, 500, 600, 700, 800, 300], 901),
                               ([0, 0, 0, 0, 5, 7, 10], [0, 5, 0, 7, 0, 10, 0], 11),
                               ([0, 0, 2, 36, 36, 70, 88, 90], [36, 2, 36, 70, 88, 0, 90, 0], 100)]

        for expected, original, k in expected_and_inputs:
            result = cs.sort(original, k)
            self.assertEqual(expected, result, f"Incorrect result for k={k} and original={original}")
