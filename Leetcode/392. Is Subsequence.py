'''
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false
 

Constraints:

0 <= s.length <= 100
0 <= t.length <= 104
s and t consist only of lowercase English letters.
 

Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 109, and you want to check one by one to see if t has its subsequence. In this scenario, how would you change your code?
'''

from typing import *

import unittest


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sp = 0
        tp = 0
        while sp < len(s) and tp < len(t):
            if len(s) - sp > len(t) - tp:
                return False
            if s[sp] == t[tp]:
                sp += 1
                tp += 1
            else:
                tp += 1
        return sp == len(s)

        
class TestSolution(unittest.TestCase):
    def test_case(self):
        examples = (
            (("axc","ahbgdc"), False),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().isSubsequence(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()

