'''
Given a binary string s, return the number of substrings with all characters 1's. Since the answer may be too large, return it modulo 109 + 7.

 

Example 1:

Input: s = "0110111"
Output: 9
Explanation: There are 9 substring in total with only 1's characters.
"1" -> 5 times.
"11" -> 3 times.
"111" -> 1 time.
Example 2:

Input: s = "101"
Output: 2
Explanation: Substring "1" is shown 2 times in s.
Example 3:

Input: s = "111111"
Output: 21
Explanation: Each substring contains only 1's characters.
 

Constraints:

1 <= s.length <= 105
s[i] is either '0' or '1'.
'''
import unittest
from typing import *


class Solution:
    def numSub(self, s: str) -> int:
        start = 0
        res = 0
        for i in range(len(s) + 1):
            if i == len(s) or s[i] == '0':
                num = i - start
                res += (1 + num) * num // 2
                start = i + 1
        return res % int(1e9 + 7)

class TestSolution(unittest.TestCase):

    def test_case(self):
        examples = (
            (("0110111",),9),
        )
        for first, second in examples:
            self.assert_function(first, second)

    def assert_function(self, first, second):
        self.assertEqual(Solution().numSub(*first), second,
                         msg="first: {}; second: {}".format(first, second))


unittest.main()