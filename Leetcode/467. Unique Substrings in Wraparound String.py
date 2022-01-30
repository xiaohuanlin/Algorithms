'''
We define the string s to be the infinite wraparound string of "abcdefghijklmnopqrstuvwxyz", so s will look like this:

"...zabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcd....".
Given a string p, return the number of unique non-empty substrings of p are present in s.

 

Example 1:

Input: p = "a"
Output: 1
Explanation: Only the substring "a" of p is in s.
Example 2:

Input: p = "cac"
Output: 2
Explanation: There are two substrings ("a", "c") of p in s.
Example 3:

Input: p = "zab"
Output: 6
Explanation: There are six substrings ("z", "a", "b", "za", "ab", and "zab") of p in s.
 

Constraints:

1 <= p.length <= 105
p consists of lowercase English letters.
'''
from typing import *

import unittest


class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        start = 0
        classify = [0 for _ in range(26)]

        index = ord(p[0]) - ord('a')
        classify[index] = 1
        for i in range(1, len(p)):
            index = ord(p[i]) - ord('a')
            prev_index = ord(p[i - 1]) - ord('a') 

            if index == (prev_index + 1) % 26:
                classify[index] = max(i - start + 1, classify[index])
            else:
                classify[index] = max(1, classify[index])
                start = i

        index = ord(p[-1]) - ord('a')
        classify[index] = max(len(p) - start, classify[index])

        res = 0
        for num in classify:
            res += num
        return res


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (("zab",), 6),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().findSubstringInWraproundString(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
