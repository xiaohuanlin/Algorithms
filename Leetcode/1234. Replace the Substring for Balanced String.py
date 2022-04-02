'''
You are given a string s of length n containing only four kinds of characters: 'Q', 'W', 'E', and 'R'.

A string is said to be balanced if each of its characters appears n / 4 times where n is the length of the string.

Return the minimum length of the substring that can be replaced with any other string of the same length to make s balanced. If s is already balanced, return 0.

 

Example 1:

Input: s = "QWER"
Output: 0
Explanation: s is already balanced.
Example 2:

Input: s = "QQWE"
Output: 1
Explanation: We need to replace a 'Q' to 'R', so that "RQWE" (or "QRWE") is balanced.
Example 3:

Input: s = "QQQW"
Output: 2
Explanation: We can replace the first "QQ" to "ER". 
 

Constraints:

n == s.length
4 <= n <= 105
n is a multiple of 4.
s contains only 'Q', 'W', 'E', and 'R'.
'''
from typing import *

import unittest

from collections import Counter

class Solution:
    def balancedString(self, s: str) -> int:
        maps = {}
        for k, v in Counter(s).items():
            if v > len(s) // 4:
                 maps[k] = v - len(s) // 4
        if not maps:
            return 0
        
        res = len(s)
        left = 0
        for i in range(len(s)):
            if s[i] not in maps:
                continue
                
            maps[s[i]] -= 1
            while all(v <= 0 for v in maps.values()):
                if s[left] in maps:
                    maps[s[left]] += 1
                res = min(res, i - left + 1)
                left += 1

        return res



class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (("QWER", ), 0),
            (("QQWE", ), 1),
            (("QQQW", ), 2),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().balancedString(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
