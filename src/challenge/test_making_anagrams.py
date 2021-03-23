import unittest
import making_anagrams as ma


class TestMakingAnagrams(unittest.TestCase):
    def test_making_anagrams(self):
        test_cases = [(2, "cde", "dcf"),
                      (4, "cde", "abc"),
                      (30, "fcrxzwscanmligyxyvym", "jxwtrhvujlmrpdoqbisbwhmgpmeoke")]
        for expected, a, b, in test_cases:
            self.assertEqual(expected, ma.calculate_minimum_deletions(a, b))
