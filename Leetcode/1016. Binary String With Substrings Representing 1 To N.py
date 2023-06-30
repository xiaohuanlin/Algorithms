'''
Given a binary string s and a positive integer n, return true if the binary representation of all the integers in the range [1, n] are substrings of s, or false otherwise.

A substring is a contiguous sequence of characters within a string.

 

Example 1:

Input: s = "0110", n = 3
Output: true
Example 2:

Input: s = "0110", n = 4
Output: false
 

Constraints:

1 <= s.length <= 1000
s[i] is either '0' or '1'.
1 <= n <= 109
'''
from typing import *

import unittest


class Solution:
    def queryString(self, s: str, n: int) -> bool:
        sets = set()
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                sets.add(int(s[i:j], base=2))
        for i in range(1, n + 1):
            if i not in sets:
                return False
        return True
        
        
class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (("0110",3),True),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().queryString(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()
