import unittest
import is_palindrome as ip


class IsPalindromeTest(unittest.TestCase):

    def test_something(self):
        test_cases = [(True, "racecar"), (True, "91019"), (True, "a"), (True, "aa"), (True, "aaa"), (True, "aaaa"),
                      (False, "aaaaaabaaaaa"), (False, "abcbba"), (True, "In girum imus nocte et consumimur igni")]
        for expected, str_input in test_cases:
            self.assertEqual(expected, ip.is_palindrome(str_input), f"'{str_input}' should return '{expected}'")
