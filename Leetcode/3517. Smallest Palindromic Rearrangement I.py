'''
You are given a palindromic string s.

Return the lexicographically smallest palindromic permutation of s.



Example 1:

Input: s = "z"

Output: "z"

Explanation:

A string of only one character is already the lexicographically smallest palindrome.

Example 2:

Input: s = "babab"

Output: "abbba"

Explanation:

Rearranging "babab" → "abbba" gives the smallest lexicographic palindrome.

Example 3:

Input: s = "daccad"

Output: "acddca"

Explanation:

Rearranging "daccad" → "acddca" gives the smallest lexicographic palindrome.



Constraints:

1 <= s.length <= 105
s consists of lowercase English letters.
s is guaranteed to be palindromic.
'''
import unittest

from typing import *
from collections import Counter


class Solution:
    def smallestPalindrome(self, s: str) -> str:
        c = Counter(s)
        res = ['' for _ in range(len(s))]
        i = 0
        for k, v in sorted(c.items()):
            if v % 2 != 0:
                res[len(res)//2] = k
                c[k] -= 1
            cnt = v // 2
            for m in range(cnt):
                res[i+m] = k
                res[len(res)-1-i-m] = k
            i += cnt
        return ''.join(res)


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (("babab",),"abbba"),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().smallestPalindrome(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()

