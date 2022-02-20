'''
Given two strings s and t, return the number of distinct subsequences of s which equals t.

A string's subsequence is a new string formed from the original string by deleting some (can be none) of the characters without disturbing the remaining characters' relative positions. (i.e., "ACE" is a subsequence of "ABCDE" while "AEC" is not).

The test cases are generated so that the answer fits on a 32-bit signed integer.

 

Example 1:

Input: s = "rabbbit", t = "rabbit"
Output: 3
Explanation:
As shown below, there are 3 ways you can generate "rabbit" from S.
rabbbit
rabbbit
rabbbit
Example 2:

Input: s = "babgbag", t = "bag"
Output: 5
Explanation:
As shown below, there are 5 ways you can generate "bag" from S.
babgbag
babgbag
babgbag
babgbag
babgbag
 

Constraints:

1 <= s.length, t.length <= 1000
s and t consist of English letters.
'''

from typing import *
from pprint import pprint

import unittest

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # dp[i][j] means starting test from s[i:] and t[j:]
        dp = [[0 for _ in range(len(t))] for _ in range(len(s) + 1)]
        for i in range(len(s) - 1, -1, -1):
            dp[i][len(t) - 1] = dp[i + 1][len(t) - 1]
            if s[i] == t[-1]:
                dp[i][len(t) - 1] += 1

        for i in range(len(s) - 1, -1, -1):
            for j in range(len(t) - 2, -1, -1):
                dp[i][j] = dp[i + 1][j]
                if s[i] == t[j]:
                    dp[i][j] += dp[i + 1][j + 1]
        return dp[0][0]


class TestSolution(unittest.TestCase):
    def test_case(self):
        examples = (
            (("rabbbit", "rabbit"), 3),
            (("babgbag", "bag"), 5),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().numDistinct(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()

