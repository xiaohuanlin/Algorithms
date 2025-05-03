'''
Given a string s of length n and an integer k, determine whether it is possible to select k disjoint special substrings.

A special substring is a substring where:

Any character present inside the substring should not appear outside it in the string.
The substring is not the entire string s.
Note that all k substrings must be disjoint, meaning they cannot overlap.

Return true if it is possible to select k such disjoint special substrings; otherwise, return false.

 

Example 1:

Input: s = "abcdbaefab", k = 2

Output: true

Explanation:

We can select two disjoint special substrings: "cd" and "ef".
"cd" contains the characters 'c' and 'd', which do not appear elsewhere in s.
"ef" contains the characters 'e' and 'f', which do not appear elsewhere in s.
Example 2:

Input: s = "cdefdc", k = 3

Output: false

Explanation:

There can be at most 2 disjoint special substrings: "e" and "f". Since k = 3, the output is false.

Example 3:

Input: s = "abeabe", k = 0

Output: true

 

Constraints:

2 <= n == s.length <= 5 * 104
0 <= k <= 26
s consists only of lowercase English letters.
'''
import unittest

from typing import *


class Solution:
    def maxSubstringLength(self, s: str, k: int) -> bool:
        first = {}
        end = {}
        for i in range(len(s)):
            if s[i] not in first:
                first[s[i]] = i
            end[s[i]] = i

        for f in first:
            for i in range(first[f], end[f]):
                first[f] = min(first[f], first[s[i]])
                end[f] = max(end[f], end[s[i]])

        dp = [0] * (len(s) + 1)
        for i in range(len(s)):
            dp[i+1] = dp[i]
            if end[s[i]] == i and (first[s[i]] != 0 or i != len(s) - 1):
                dp[i+1] = max(dp[i+1], 1 + dp[first[s[i]]])
        return dp[-1] >= k


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (("abcdbaefab", 2), True),
            (("cdefdc", 3), False),
            (("abeabe", 0), True),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().maxSubstringLength(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()

