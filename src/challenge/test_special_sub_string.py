import unittest
import special_sub_string as sss


class TestSpecialSubString(unittest.TestCase):

    def test_special_sub_string(self):
        test_cases = [(12, "mnonopoo"), (10, "aaaa"), (10, "abcbaba"), (7, "asasd"), (16, "aaabaaa")]
        for expected, word in test_cases:
            self.assertEqual(expected, sss.count_special_sub_strings(len(word), word))

    def test_is_special_string(self):
        test_cases = [(True, "aaaaaaa"), (True, "aabaa"), (True, "bbbbabbbb"), (False, "abc"), (False, "aaaac")]
        for expected, word in test_cases:
            self.assertEqual(expected, sss.is_special(word))
