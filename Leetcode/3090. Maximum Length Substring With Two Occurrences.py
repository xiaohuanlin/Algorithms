'''
Given a string s, return the maximum length of a 
substring
 such that it contains at most two occurrences of each character.
 

Example 1:

Input: s = "bcbbbcba"

Output: 4

Explanation:

The following substring has a length of 4 and contains at most two occurrences of each character: "bcbbbcba".
Example 2:

Input: s = "aaaa"

Output: 2

Explanation:

The following substring has a length of 2 and contains at most two occurrences of each character: "aaaa".
 

Constraints:

2 <= s.length <= 100
s consists only of lowercase English letters.
'''
import unittest

from typing import *
from collections import Counter


from collections import Counter

class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        left = 0
        windows = Counter()
        res = 0
        for right in range(len(s)):
            windows[s[right]] += 1
            while left < right and windows.most_common(1)[0][1] > 2:
                windows[s[left]] -= 1
                left += 1
            res = max(res, right - left + 1)
        return res


class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (("bcbbbcba", ), 4),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().maximumLengthSubstring(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
