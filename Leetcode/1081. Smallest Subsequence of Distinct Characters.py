'''
Given a string s, return the lexicographically smallest subsequence of s that contains all the distinct characters of s exactly once.

 

Example 1:

Input: s = "bcabc"
Output: "abc"
Example 2:

Input: s = "cbacdcbc"
Output: "acdb"
 

Constraints:

1 <= s.length <= 1000
s consists of lowercase English letters.
 

Note: This question is the same as 316: https://leetcode.com/problems/remove-duplicate-letters/
'''

from typing import *

import unittest


class Solution:
    def smallestSubsequence(self, s: str) -> str:
        counts = [0 for _ in range(26)]
        for i in range(len(s)):
            counts[ord(s[i]) - ord('a')] += 1
        
        stack = []
        for i in range(len(s)):
            k = ord(s[i]) - ord('a')
            counts[k] -= 1
            if s[i] in stack:
                continue
            while stack and stack[-1] >= s[i] and counts[ord(stack[-1]) - ord('a')] > 0:
                stack.pop()
            stack.append(s[i])
        return ''.join(stack)
        
class TestSolution(unittest.TestCase):
    def test_case(self):
        examples = (
            (("cbacdcbc",),"acdb"),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().smallestSubsequence(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()

