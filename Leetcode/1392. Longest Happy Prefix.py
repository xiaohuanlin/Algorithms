'''
A string is called a happy prefix if is a non-empty prefix which is also a suffix (excluding itself).

Given a string s, return the longest happy prefix of s. Return an empty string "" if no such prefix exists.

 

Example 1:

Input: s = "level"
Output: "l"
Explanation: s contains 4 prefix excluding itself ("l", "le", "lev", "leve"), and suffix ("l", "el", "vel", "evel"). The largest prefix which is also suffix is given by "l".
Example 2:

Input: s = "ababab"
Output: "abab"
Explanation: "abab" is the largest prefix which is also suffix. They can overlap in the original string.
 

Constraints:

1 <= s.length <= 105
s contains only lowercase English letters.
'''
import unittest

from typing import *

class Solution:
    def longestPrefix(self, s: str) -> str:
        lps = [0] * len(s)
        i = 0
        for j in range(1, len(s)):
            while i > 0 and s[i] != s[j]:
                i = lps[i-1]
            if s[i] == s[j]:
                i += 1
            lps[j] = i

        return s[:i]


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (("level",), "l"),
            (("ababab",), "abab"),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().longestPrefix(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()

