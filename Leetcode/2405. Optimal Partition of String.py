'''
Given a string s, partition the string into one or more substrings such that the characters in each substring are unique. That is, no letter appears in a single substring more than once.

Return the minimum number of substrings in such a partition.

Note that each character should belong to exactly one substring in a partition.

 

Example 1:

Input: s = "abacaba"
Output: 4
Explanation:
Two possible partitions are ("a","ba","cab","a") and ("ab","a","ca","ba").
It can be shown that 4 is the minimum number of substrings needed.
Example 2:

Input: s = "ssssss"
Output: 6
Explanation:
The only valid partition is ("s","s","s","s","s","s").
 

Constraints:

1 <= s.length <= 105
s consists of only English lowercase letters.
'''
import unittest

from typing import *

class Solution:
    def partitionString(self, s: str) -> int:
        sets = set()
        cnt = 1
        for c in s:
            if c in sets:
                cnt += 1
                sets = set()
            sets.add(c)
        return cnt


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (("abacaba",), 4),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().partitionString(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
