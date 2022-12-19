'''
You are given two strings s and t consisting of only lowercase English letters.

Return the minimum number of characters that need to be appended to the end of s so that t becomes a subsequence of s.

A subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.

 

Example 1:

Input: s = "coaching", t = "coding"
Output: 4
Explanation: Append the characters "ding" to the end of s so that s = "coachingding".
Now, t is a subsequence of s ("coachingding").
It can be shown that appending any 3 characters to the end of s will never make t a subsequence.
Example 2:

Input: s = "abcde", t = "a"
Output: 0
Explanation: t is already a subsequence of s ("abcde").
Example 3:

Input: s = "z", t = "abcde"
Output: 5
Explanation: Append the characters "abcde" to the end of s so that s = "zabcde".
Now, t is a subsequence of s ("zabcde").
It can be shown that appending any 4 characters to the end of s will never make t a subsequence.
 

Constraints:

1 <= s.length, t.length <= 105
s and t consist only of lowercase English letters.
'''
import unittest

from typing import *

class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        start = 0
        for i in range(len(t)):
            target = t[i]
            while start < len(s) and s[start] != target:
                start += 1
            if start >= len(s):
                return len(t) - i
            start += 1
        return 0


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (("abcde", "a"), 0),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().appendCharacters(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
