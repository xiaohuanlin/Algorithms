'''
Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

 

Example 1:

Input: s = "aab"
Output: 1
Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.
Example 2:

Input: s = "a"
Output: 0
Example 3:

Input: s = "ab"
Output: 1
 

Constraints:

1 <= s.length <= 2000
s consists of lowercase English letters only.
'''
from audioop import minmax
from typing import *

import unittest
from pprint import pprint


class Solution:
    def minCut(self, s: str) -> int:
        return self.minCount(s, 0, {}, {})

    def isPalindrome(self, s, i, j, mem):
        if i >= j:
            return True

        key = (i, j)
        if key in mem:
            return mem[key]
        
        if s[i] == s[j]:
            mem[key] = self.isPalindrome(s, i + 1, j - 1, mem)
            return mem[key]
        return False
    
    def minCount(self, s, i, mem, min_mem):
        if i >= len(s) - 1:
            return 0

        if i in min_mem:
            return min_mem[i]

        if self.isPalindrome(s, i, len(s) - 1, mem):
            min_mem[i] = 0
            return 0

        min_count = float('+inf')
        for k in range(i, len(s)):
            if self.isPalindrome(s, i, k, mem):
                min_count = min(min_count, self.minCount(s, k + 1, mem, min_mem) + 1)
        min_mem[i] = min_count
        return min_count
                


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (("bbcbcb", ), 1),
            (("asdasdnasdjaskd", ), 14),
            (("aab", ), 1),
            (("a", ), 0),
            (("ab", ), 1),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().minCut(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
