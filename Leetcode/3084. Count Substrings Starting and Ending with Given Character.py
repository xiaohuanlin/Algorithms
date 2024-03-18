'''
You are given a string s and a character c. Return the total number of
substrings
 of s that start and end with c.



Example 1:

Input: s = "abada", c = "a"

Output: 6

Explanation: Substrings starting and ending with "a" are: "abada", "abada", "abada", "abada", "abada", "abada".

Example 2:

Input: s = "zzz", c = "z"

Output: 6

Explanation: There are a total of 6 substrings in s and all start and end with "z".



Constraints:

1 <= s.length <= 105
s and c consist only of lowercase English letters.
'''
import unittest

from typing import *


class Solution:
    def countSubstrings(self, s: str, c: str) -> int:
        count = s.count(c)
        return count + (count - 1) * count // 2


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (("abada", "a"), 6),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().countSubstrings(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
