'''
An alphabetical continuous string is a string consisting of consecutive letters in the alphabet. In other words, it is any substring of the string "abcdefghijklmnopqrstuvwxyz".

For example, "abc" is an alphabetical continuous string, while "acb" and "za" are not.
Given a string s consisting of lowercase letters only, return the length of the longest alphabetical continuous substring.



Example 1:

Input: s = "abacaba"
Output: 2
Explanation: There are 4 distinct continuous substrings: "a", "b", "c" and "ab".
"ab" is the longest continuous substring.
Example 2:

Input: s = "abcde"
Output: 5
Explanation: "abcde" is the longest continuous substring.


Constraints:

1 <= s.length <= 105
s consists of only English lowercase letters.
'''
import unittest

from typing import *

class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        cnt = 0
        res = 0
        for i in range(1, len(s)):
            if ord(s[i]) - ord(s[i-1]) == 1:
                cnt += 1
            else:
                res = max(res, cnt)
                cnt = 0
        res = max(res, cnt)
        return res + 1


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (("abacaba",),2),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().longestContinuousSubstring(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
