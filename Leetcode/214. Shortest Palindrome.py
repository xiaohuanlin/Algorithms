'''
You are given a string s. You can convert s to a palindrome by adding characters in front of it.

Return the shortest palindrome you can find by performing this transformation.

 

Example 1:

Input: s = "aacecaaa"
Output: "aaacecaaa"
Example 2:

Input: s = "abcd"
Output: "dcbabcd"
 

Constraints:

0 <= s.length <= 5 * 104
s consists of lowercase English letters only.
'''
from typing import *
from pprint import pprint

import unittest


class Solution:
    def shortestPalindrome(self, s: str) -> str:
        reverse_s = s[::-1]
        for i in range(len(s)):
            if s.startswith(reverse_s[i:]):
                return reverse_s[:i] + s
        return ""


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (("abba",), "abba"),
            (("aba",), "aba"),
            (("aacecaaa",), "aaacecaaa"),
            (("abcd",), "dcbabcd"),
            (("a",), "a"),
            (("",), "")
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().shortestPalindrome(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
